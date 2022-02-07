from urllib import request
from django.db import models
from django.conf import settings
from mainapp.models import Products


class BasketManager(models.Manager):
    def count(self):
        return len(self.all())
    
    def total_cost(self):
        get_basket = self.all()
        return sum(item.quantity * item.product.price for item in get_basket)
class Basket(models.Model):
    class Meta:
        unique_together = ['user', 'product']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    objects = BasketManager()

    def __str__(self):
        return (f'{self.user} {self.product}')