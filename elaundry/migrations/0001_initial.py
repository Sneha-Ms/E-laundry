# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-23 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rollNo', models.IntegerField()),
                ('password', models.TextField()),
                ('hostel', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('mobileNumber', models.IntegerField()),
            ],
        ),
    ]
