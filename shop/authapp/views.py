from django.shortcuts import render, HttpResponseRedirect
from mainapp.views import MENU_LINKS
from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm
from django.contrib import auth
from django.urls import reverse

def login(request): 
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        login_form = UserLoginForm()
    return render(request, 'authapp/login.html', context={
        'title': 'Войти',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
        'login_form': login_form
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')     


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
    
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()
    
    content = {
        'register_form': register_form,
        'title': 'Личный кабинет',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
    }
    
    return render(request, 'authapp/register.html', content)


def edit(request):
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
    
    content = {
        'edit_form': edit_form,
        'title': 'Личный кабинет',
        'class_name': 'hero-white',
        'menu_links': MENU_LINKS,
    }
    
    return render(request, 'authapp/edit.html', content)

