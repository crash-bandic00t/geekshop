from django.core.management.base import BaseCommand
from main.models import ProductTypes, Products
from authapp.models import ShopUser

import json, os

JSON_PATH = 'main/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')          

        ProductTypes.objects.all().delete()
        for category in categories:
            new_category = ProductTypes(**category)
            new_category.save()        
        
        products = load_from_json('products')
        
        Products.objects.all().delete()
        for product in products:
            category_name = product["product_type"]
            # Получаем категорию по имени
            _category = ProductTypes.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['product_type'] = _category
            new_product = Products(**product)
            new_product.save()

        # # Создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.create_superuser('admin', 'admin@localhost', '123', age=29)
