from pdb import Pdb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Products
from .models import Basket
from django.http import JsonResponse


@login_required
def basket(request):
    return render(request, 'basketapp/basket.html', context={
        'title': 'Корзина',
        'class_name': 'hero-white',
    })


@login_required
def basket_add(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    obj, created = Basket.objects.get_or_create(
        user=request.user, product=product)
    if not created:
        obj.quantity += 1
        obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, user_product_id):
    user_product = get_object_or_404(Basket, id=user_product_id)
    user_product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, user_product_id, user_product_quantity):
    user_product = get_object_or_404(Basket, id=user_product_id)
    if user_product_quantity > 0:
        user_product.quantity = user_product_quantity
        user_product.save()
        content = {
            'cost': user_product.cost(),
            'total_cost': request.user.basket.total_cost()
        }
    else:
        user_product.delete()
        content = {
            'delete': True,
            'total_cost': request.user.basket.total_cost()
        }
    return JsonResponse({'content': content})
