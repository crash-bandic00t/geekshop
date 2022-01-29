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
    get_product_types = ProductTypes.objects.all()
    return render(request, 'main/products.html', context={
        'title': 'Продукты',
        'menu': header_menu,
        'products': products,
        'product_types': get_product_types
    })

def product_type (request, prod_type):
    get_product_types = ProductTypes.objects.all()
    get_type = get_object_or_404(ProductTypes, slug=prod_type)
    get_products_by_type = Products.objects.filter(product_type=get_type.id)[:3]
    return render(request, 'main/product_by_types.html', context={
        'title': 'Продукты',
        'menu': header_menu,
        'products': get_products_by_type,
        'product_types': get_product_types,
        'prod_type': get_type.name
    })
