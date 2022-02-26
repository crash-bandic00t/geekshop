from django.shortcuts import get_object_or_404, render
from .models import *
import random


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'class_name': 'slider',
    })


def products(request):
    get_products = Products.objects.all()
    get_categories = Category.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'class_name': 'hero-white',
        'products': random.choices(get_products, k=3),
        'categories': get_categories
    })


def product_detail(request, category, product_id):
    get_product = get_object_or_404(Products, id=product_id)
    return render(request, 'mainapp/product-detail.html', context={
        'title': get_product.category.name,
        'class_name': 'hero-white',
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
        'products': get_products,
        'categories': get_categories,
        'category_name': category_name,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'class_name': 'hero',
    })
