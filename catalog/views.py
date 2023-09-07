from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/dought_card.html', {'products': products})


def product_detail(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/item.html', {'product': item})


def contacts(request):
    return render(request, 'catalog/contacts.html')
