from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **kwargs):
        # Очистка данных в базе данных
        Category.objects.all().delete()
        Product.objects.all().delete()
        # Создание категорий
        for category_num in range(1, 11):
            name = f"Категория {category_num}"
            description = f"Описание категории {category_num}"
            category = Category.objects.create(name=name, description=description)

            # Создание продуктов для каждой категории
            for product_num in range(1, 6):
                product_name = f"Продукт {product_num}"
                product_description = f"Описание продукта {product_num}\nКатегории {category_num}"
                price = round(random.uniform(1, 1000), 2)

                Product.objects.create(
                    name=product_name,
                    description=product_description,
                    category=category,
                    price=price
                )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными'))
