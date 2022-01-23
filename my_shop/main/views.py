from django.shortcuts import render

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
    return render(request, 'main/products.html', context={
        'title': 'Продукты',
        'menu': header_menu,
        'products': products,
    })