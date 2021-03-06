from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from .models import User
from .models import UserProfile

import hashlib
import os


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1',
                  'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self):
        user = super().save()
        user.is_active = False
        user.activation_key = hashlib.md5(
            user.email.encode('utf-8') + os.urandom(64)
        ).hexdigest()
        user.save()

        return user

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise ValidationError("Вы слишком молоды!")

        return data


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',
                  'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise ValidationError("Вы слишком молоды!")

        return data

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['aboutMe'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-select'
        self.fields['gender'].empty_label = 'Выберите пол'

        
