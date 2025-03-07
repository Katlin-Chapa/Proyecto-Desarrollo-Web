<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>Q. {{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>Q. {{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>Q. {{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Detalles de envío</h2>

                <p class="has-text-grey mb-4">* Todos los campos son obligatorios</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Nombre*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Apellido*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Correo electrónico*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email" @blur="validateEmail">
                            </div>
                            <p class="help is-danger" v-if="emailError">{{ emailError }}</p>
                        </div>

                        <div class="field">
                            <label>Teléfono*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone" @blur="validatePhone">
                            </div>
                            <p class="help is-danger" v-if="phoneError">{{ phoneError }}</p>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Dirección*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Código postal*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode" @blur="validateZipcode">
                            </div>
                            <p class="help is-danger" v-if="zipcodeError">{{ zipcodeError }}</p>
                        </div>

                        <div class="field">
                            <label>Lugar*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Pagar con Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Ferretería'  

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51QDfqzLSSND5dmdGshJtJheS0xsG6Tk4WM68n37GeDkyvDBGDrirmyML9qyhWl8kPc6H8HQGeWewY0F6YH3wfGID00LrotTArY')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        validateEmail() {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            this.emailError = !emailPattern.test(this.email) ? 'Por favor ingresa un correo electrónico válido.' : '';
        },
        validatePhone() {
            const phonePattern = /^[0-9]*$/; 
            this.phoneError = !phonePattern.test(this.phone) ? 'El número de teléfono solo puede contener números.' : '';
        },
        validateZipcode() {
            const zipcodePattern = /^[0-9]*$/; 
            this.zipcodeError = !zipcodePattern.test(this.zipcode) ? 'El código postal solo puede contener números.' : '';
        },
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.validateEmail();
            this.validatePhone();
            this.validateZipcode();
            this.errors = []

            if (this.emailError || this.phoneError || this.zipcodeError) {
                this.errors.push('Revisa los campos del formulario')
                return;
            }

            if (this.first_name === '') {
                this.errors.push('¡Falta el campo del nombre!')
            }

            if (this.last_name === '') {
                this.errors.push('¡Falta el campo del apellido!')
            }

            if (this.email === '') {
                this.errors.push('¡Falta el campo del correo electrónico!')
            }

            if (this.phone === '') {
                this.errors.push('¡Falta el campo del teléfono!')
            }

            if (this.address === '') {
                this.errors.push('¡Falta el campo de la dirección!')
            }

            if (this.zipcode === '') {
                this.errors.push('¡Falta el campo del código postal!')
            }

            if (this.place === '') {
                this.errors.push('¡Falta el campo del lugar!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)

                        this.errors.push('Algo salió mal con Stripe. Por favor, intenta de nuevo.')

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Algo salió mal. Por favor, intenta de nuevo.')

                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>
