import os
import random
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.conf import settings

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

                # Выбор случайного изображения из папки media
                media_dir = settings.MEDIA_ROOT
                image_files = [f for f in os.listdir(media_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
                if image_files:
                    random_image = random.choice(image_files)
                else:
                    random_image = None

                Product.objects.create(
                    name=product_name,
                    description=product_description,
                    category=category,
                    price=price,
                    img=random_image  # Добавляем случайное изображение
                )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными'))
