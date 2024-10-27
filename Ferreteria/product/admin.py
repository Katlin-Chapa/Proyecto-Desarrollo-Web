from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price', 'date_added')
    list_filter = ('category', 'date_added', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
