# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_passwordreset', '0003_resetpasswordtoken_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetpasswordtoken',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
