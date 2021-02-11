from django.contrib import admin
from challenge.category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
