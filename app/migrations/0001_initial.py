# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdata', models.TextField(verbose_name='Строка')),
            ],
        ),
    ]
