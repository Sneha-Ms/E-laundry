# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-24 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_register_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='mailId',
            field=models.TextField(default='a@pqrs.com'),
            preserve_default=False,
        ),
    ]
