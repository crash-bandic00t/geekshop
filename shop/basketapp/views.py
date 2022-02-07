from pdb import Pdb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.views import MENU_LINKS
from mainapp.models import Products
from .models import Basket


@login_required
def basket(request):
    return render(request, 'basketapp/basket.html', context={
        'title': 'Корзина',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS
    })

@login_required
def basket_add(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    obj, created = Basket.objects.get_or_create(user=request.user, product=product)
    if not created:
        obj.quantity += 1
        obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_delete(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    