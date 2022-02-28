from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_activation_key_expitarion_date():
    return timezone.localtime() + timedelta(hours=48)


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50, blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expire = models.DateTimeField(
        default=get_activation_key_expitarion_date
    )

    def is_activation_key_expired(self):
        if timezone.localtime() <= self.activation_key_expire:
            return False
        else:
            return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(User, null=False,
                                db_index=True, on_delete=models.CASCADE, related_name='profile')
    aboutMe = models.TextField(verbose_name='о себе', max_length=512,
                               blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1,
                              choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

