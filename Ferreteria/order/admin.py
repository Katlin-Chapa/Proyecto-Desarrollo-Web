from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price',)

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'address',
        'place', 'phone', 'paid_amount', 'created_at'
    )
    list_filter = ('created_at', 'user')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
