# Generated by Django 3.2.12 on 2022-02-21 12:56

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_user_activation_key_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=authapp.models.get_activation_key_expitarion_date),
        ),
    ]
