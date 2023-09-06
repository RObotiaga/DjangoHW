from django.shortcuts import render
from catalog.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/dought_card.html', {'products': products})


def contacts(request):
    return render(request, 'catalog/contacts.html')
