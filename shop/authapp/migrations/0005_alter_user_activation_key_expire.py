# Generated by Django 4.0.2 on 2022-02-21 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 12, 9, 59, 669268, tzinfo=utc)),
        ),
    ]
