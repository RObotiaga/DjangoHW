from django.urls import path
from . import views

app_name = 'catalog'  # Устанавливаем пространство имён

urlpatterns = [
    path('home/', views.home),
    path('contacts/', views.contacts)
]
