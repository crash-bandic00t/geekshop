from pdb import Pdb
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.views import MENU_LINKS
from mainapp.models import Products
from .models import Basket


def basket(request):
    get_user_products = Basket.objects.filter(user=request.user)
    get_full_price = Basket.objects.basket_sum_price(request.user)
    # import pdb
    # pdb.set_trace()
    return render(request, 'basketapp/basket.html', context={
        'user_products': get_user_products,
        'title': 'Корзина',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
        'full_price': get_full_price
    })

def basket_add(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    obj, created = Basket.objects.get_or_create(user=request.user, product=product)
    if not created:
        obj.quantity += 1
        obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    