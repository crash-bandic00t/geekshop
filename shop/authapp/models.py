from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveIntegerField(verbose_name = 'Возраст')   
    city = models.CharField(verbose_name='Город', max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
