from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.CharField(max_length=150, verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f'{self.name} \n{self.description}'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', null=True, blank=True)
    img = models.ImageField(upload_to='products/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'