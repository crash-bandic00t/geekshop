from django.urls import URLPattern, path
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<slug:category>', views.product_by_categoty, name='products-by-category'),
    path('contact/', views.contact, name='contact'),
]