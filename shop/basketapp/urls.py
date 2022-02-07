from django.urls import path
from . import views

app_name = 'basketapp'
urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:product_id>', views.basket_add, name='basket-add'),
    path('delete/<int:product_id>', views.basket_delete, name='basket-delete'),
]