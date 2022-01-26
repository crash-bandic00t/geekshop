from django.core.management.base import BaseCommand
from main.models import ProductTypes, Products
from django.contrib.auth.models import User

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
            print(new_category.slug)
        #     new_category.save()        
        
        # products = load_from_json('products')
        
        # Products.objects.all().delete()
        # for product in products:
        #     category_name = product["category"]
        #     # Получаем категорию по имени
        #     _category = ProductTypes.objects.get(name=category_name)
        #     # Заменяем название категории объектом
        #     product['category'] = _category
        #     new_product = Products(**product)
        #     new_product.save()

        # # Создаем суперпользователя при помощи менеджера модели
        # super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')