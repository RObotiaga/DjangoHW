from django.contrib import admin
from catalog.models import Product, Category


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
