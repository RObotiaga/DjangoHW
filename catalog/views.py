from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView
from catalog.forms import CreateProductForm, VersionForm


class HomeView(ListView):
    model = Product
    template_name = 'catalog/card_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        return context

class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('catalog:home')

def add_version(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            version.save()
            return redirect('catalog:product_detail', pk=pk)
    else:
        form = VersionForm()

    return render(request, 'catalog/add_version.html', {'form': form})