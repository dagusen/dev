# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_activation_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='activation_key',
        ),
    ]
