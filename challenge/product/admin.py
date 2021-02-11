from django.contrib import admin
from challenge.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'get_categories')


admin.site.register(Product, ProductAdmin)

