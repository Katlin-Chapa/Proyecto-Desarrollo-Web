from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserProfileForm, UserForm
from .models import Account, UserProfile
from orders.models import Order
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from carts.views import _cart_id
from carts.models import Cart, CartItem
import requests

# Vista de registro
class RegistroView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]  # Asignar username a partir del email
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            profile = UserProfile(user_id=user.id, profile_picture='default/default-user.png')
            profile.save()

            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta en ByteShop para continuar'
            body = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            return redirect('/accounts/login/?command=verification&email=' + email)

        return render(request, 'accounts/register.html', {'form': form})

# Vista de inicio de sesión
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exist = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exist:
                    cart_item = CartItem.objects.filter(cart=cart)
                    product_variation = [list(item.variation.all()) for item in cart_item]

                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = [list(item.variation.all()) for item in cart_item]
                    id = [item.id for item in cart_item]

                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass

            auth.login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente')

            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Los datos son incorrectos')
            return redirect('iniciar_sesion')

# Vista de cierre de sesión
class LogoutView(LoginRequiredMixin, View):
    login_url = 'iniciar_sesion'

    def get(self, request):
        auth.logout(request)
        messages.success(request, 'Has salido de sesión')
        return redirect('iniciar_sesion')

# Vista de mis pedidos
class MisPedidosView(LoginRequiredMixin, View):
    login_url = 'iniciar_sesion'

    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
        context = {'orders': orders}
        return render(request, 'accounts/my_orders.html', context)
