from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)

from .models import Order, OrderItem


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreate(CreateView):
    model = Order


class OrderDetail(DetailView):
    model = Order


class OrderUpdate(UpdateView):
    model = Order


class OrderDelete(DeleteView):
    model = Order


def order_forming_complete(request):
    """Поменять статус заказа на В обработке"""
    pass