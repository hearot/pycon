# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='username'),
        ),
    ]
