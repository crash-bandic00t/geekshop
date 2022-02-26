from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'adminapp'
urlpatterns = [
    path('', TemplateView.as_view(
        template_name='adminapp/index.html'), name='index'),

    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/add/', views.AddCategoryView.as_view(), name='add-category'),
    path('categories/<int:id>/edit',
         views.EditCategoryView.as_view(), name='edit-category'),
    path('categories/<int:id>/delete',
         views.DeleteCategoryView.as_view(), name='delete-category'),

    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/add', views.AddProductView.as_view(), name='add-product'),
    path('products/<int:id>/edit',
         views.EditProductView.as_view(), name='edit-product'),
    path('products/<int:id>/delete',
         views.DeleteProductView.as_view(), name='delete-product'),

    path('users/', views.UsersView.as_view(), name='users'),
    path('users/add', views.AddUserView.as_view(), name='add-user'),
    path('users/<int:id>/edit', views.EditUserView.as_view(), name='edit-user'),
    path('users/<int:id>/delete', views.DeleteUserView.as_view(), name='delete-user'),
]
