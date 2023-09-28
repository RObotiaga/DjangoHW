from django.contrib.auth import views
from django.urls import path
from users.views import RegisterView, UserConfirmEmailView, send_new_password, ProfileView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('confirm-email/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_mail'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('profile/genpassword/', send_new_password, name='send_new_password'),
]