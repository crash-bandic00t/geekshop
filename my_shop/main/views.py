from django.shortcuts import render

def index(request):
    data = {
        'header_class': 'slider',
        
    }
    return render(request, 'main/index.html', data)


def contact(request):

    return render(request, 'main/contact.html')


def products(request):
    return render(request, 'main/products.html')