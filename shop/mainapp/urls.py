from django.urls import URLPattern, path
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<slug:prod_type>', views.product_type, name='prod_type'),
    path('contact/', views.contact, name='contact'),
]