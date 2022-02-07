from django.urls import URLPattern, path
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<slug:category>', views.product_by_categoty, name='products-by-category'),
    path('products/<slug:category>/<int:product_id>', views.product_detail, name='product-detail'),
    path('contact/', views.contact, name='contact'),
]