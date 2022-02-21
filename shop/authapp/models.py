from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def get_activation_key_expitarion_date():
    return timezone.localtime() + timedelta(hours=48)
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveIntegerField(verbose_name = 'Возраст')   
    city = models.CharField(verbose_name='Город', max_length=50)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expire = models.DateTimeField(default=get_activation_key_expitarion_date)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
