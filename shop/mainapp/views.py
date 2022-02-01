from django.shortcuts import render


menu_links = [
    {
        'url': 'mainapp:index',
        'name': 'домой'
    },
    {
        'url': 'mainapp:products',
        'name': 'продукты'
    },
    {
        'url': 'mainapp:contact',
        'name': 'продукты'
    }
]

def index(request):
    # import pdb
    # pdb.set_trace()
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'class_name': 'slider',
        'menu_links': menu_links
    })

def products(request):
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'class_name': 'hero-white',
        'menu_links': menu_links
    })

def product_type(request):
    pass

def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'class_name': 'hero',
        'menu_links': menu_links
    })