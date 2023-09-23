from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.CharField(max_length=150, verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f'{self.name} \n{self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', null=True, blank=True)
    img = models.ImageField(upload_to='products/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.CharField(max_length=150, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='наименование')
    active = models.BooleanField(default=True, verbose_name='статус версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
