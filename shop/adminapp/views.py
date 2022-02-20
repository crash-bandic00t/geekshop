from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from mainapp.models import Category, Products
from authapp.models import User
from .forms import AddCategoryForm, AddProductForm, AddUserForm


class CategoriesView(ListView):
    
    model = Category
    template_name = 'adminapp/categories/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'    
        return context 



class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'adminapp/categories/add-category.html'
    success_url = reverse_lazy('adminapp:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить категорию'
        
        return context 


class EditCategoryView(UpdateView):
    model = Category
    form_class = AddCategoryForm
    context_object_name = 'cat'
    template_name = 'adminapp/categories/edit-category.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:categories')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить категорию'
        
        return context 


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'adminapp/categories/delete-category.html'
    context_object_name = 'cat'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:categories')


class ProductsView(ListView):
    
    model = Products
    template_name = 'adminapp/products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'    
        return context 



class AddProductView(CreateView):
    model = Products
    form_class = AddProductForm
    template_name = 'adminapp/products/add-product.html'
    success_url = reverse_lazy('adminapp:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        
        return context 


class EditProductView(UpdateView):
    model = Products
    form_class = AddProductForm
    context_object_name = 'prod'
    template_name = 'adminapp/products/edit-product.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить продукт'
        
        return context 


class DeleteProductView(DeleteView):
    model = Products
    template_name = 'adminapp/products/delete-product.html'
    context_object_name = 'prod'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:products')


class UsersView(ListView):
    
    model = User
    template_name = 'adminapp/users/users.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'    
        return context 



class AddUserView(CreateView):
    model = User
    form_class = AddUserForm
    template_name = 'adminapp/users/add-user.html'
    success_url = reverse_lazy('adminapp:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пользователя'
        
        return context 


class EditUserView(UpdateView):
    model = User
    form_class = AddUserForm
    context_object_name = 'user'
    template_name = 'adminapp/users/edit-user.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:users')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить пользователя'
        
        return context 


class DeleteUserView(DeleteView):
    model = User
    template_name = 'adminapp/users/delete-user.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminapp:users')

    def form_valid(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())