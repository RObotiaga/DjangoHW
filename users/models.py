from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар')
    phone = models.CharField(max_length=150, verbose_name='Телефон', null=True)
    country = models.CharField(max_length=150, verbose_name='Страна', null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
