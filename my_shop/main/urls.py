from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<slug:prod_type>', views.product_type, name='prod_type'),
    path('contact/', views.contact, name='contact'),
]