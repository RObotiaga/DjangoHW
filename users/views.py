from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/customuser_form.html'
