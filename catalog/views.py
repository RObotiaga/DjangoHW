from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, View


class HomeView(ListView):
    model = Product
    template_name = 'catalog/card_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/item_detail.html'
    context_object_name = 'product'


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')
