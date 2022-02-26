from django.urls import path
from . import views

app_name = 'basketapp'
urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:product_id>', views.basket_add, name='basket-add'),
    path('delete/<int:user_product_id>',
         views.basket_delete, name='basket-delete'),
    path('edit/<int:user_product_id>/<int:user_product_quantity>',
         views.basket_edit, name='basket-edit'),
]
