from unicodedata import category
from django.shortcuts import get_object_or_404, render
from .models import *
import random


MENU_LINKS = [
    {
        'url': 'mainapp:index',
        'name': 'домой'
    },
    {
        'url': 'mainapp:products',
        'name': 'продукты',
        'url_products': 'mainapp:products-by-category'
    },
    {
        'url': 'mainapp:contact',
        'name': 'контакты'
    }
]

def index(request):
    # import pdb
    # pdb.set_trace()
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'class_name': 'slider',
        'menu_links': MENU_LINKS,
    })

def products(request):
    get_products = Products.objects.all()
    get_categories = Category.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
        'products': random.choices(get_products, k=3),
        'categories': get_categories,
    })

def product_detail(request, category, product_id):
    get_product = get_object_or_404(Products, id=product_id)
    return render(request, 'mainapp/product-detail.html', context={
        'title': get_product.category.name,
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
        'product': get_product
    })   

def product_by_categoty(request, category):
    get_category = Category.objects.get(slug=category)
    category_name = get_category.name
    get_products = Products.objects.filter(category=get_category)[:3]
    get_categories = Category.objects.all()
    return render(request, 'mainapp/products-by-category.html', context={
        'title': 'Продукты',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
        'products': get_products,
        'categories': get_categories,
        'category_name': category_name,
    })

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'class_name': 'hero',
        'menu_links': MENU_LINKS,
    })