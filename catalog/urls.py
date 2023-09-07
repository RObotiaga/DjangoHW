from django.urls import path
from . import views

app_name = 'catalog'  # Устанавливаем пространство имён

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
