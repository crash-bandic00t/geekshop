from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


header_menu = [
    {'url':'index', 'name':'домой'},
    {'url':'products', 'name':'продукты'},
    {'url':'contact', 'name':'контакты'},
]

def index(request):
    return render(request, 'main/index.html', context={
        'title': 'Главная',
        'menu': header_menu
    })


def contact(request):

    return render(request, 'main/contact.html', context={
         'title': 'Контакты',
         'menu': header_menu
    })


def products(request):
    products = [
        {
            'name': 'Лампа 1',
            'desc': 'Классная лампа!',
            'image': 'img/product-11.jpg'
        },
        {
            'name': 'Стул',
            'desc': 'Супер стул!',
            'image': 'img/product-21.jpg'
        },
        {
            'name': 'Лампа 2',
            'desc': 'Офигенная лампа!',
            'image': 'img/product-31.jpg'
        }
    ]
    get_product_types = ProductTypes.objects.all()
    return render(request, 'main/products.html', context={
        'title': 'Продукты',
        'menu': header_menu,
        'products': products,
        'product_types': get_product_types
    })

def product_type (request, prod_type):
    get_product_types = ProductTypes.objects.all()
    get_type_id = get_object_or_404(ProductTypes, slug=prod_type).id
    get_products_by_type = Products.objects.filter(product_type=get_type_id)[:3]
    return render(request, 'main/product_by_types.html', context={
        'title': 'Продукты',
        'menu': header_menu,
        'products': get_products_by_type,
        'product_types': get_product_types
    })
