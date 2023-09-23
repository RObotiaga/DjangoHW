from django.contrib import admin
from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ()
    search_fields = ('id', 'name',)


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('id', 'name', 'description', 'category', 'price',)


@admin.register(Version)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'number', 'active',)
    list_filter = ('product',)
    search_fields = ('product', 'name', 'active',)
