from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm
from .models import User
from django.contrib import auth
from django.urls import reverse
from basketapp.models import Basket
from .utils import send_verify_mail


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
        'login_form': login_form
    })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            send_verify_mail(user)
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    content = {
        'register_form': register_form,
        'title': 'Личный кабинет',
        'class_name': 'hero-white',
    }

    return render(request, 'authapp/register.html', content)


def edit(request):
    if request.method == 'POST':
        edit_form = UserEditForm(
            request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)

    content = {
        'edit_form': edit_form,
        'title': 'Личный кабинет',
        'class_name': 'hero-white'
    }

    return render(request, 'authapp/edit.html', content)


def verify(request, email, activation_key):

    user = get_object_or_404(User, email=email)
    if user.activation_key == activation_key and not user.is_activation_key_expired():
        user.is_active = True
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')
