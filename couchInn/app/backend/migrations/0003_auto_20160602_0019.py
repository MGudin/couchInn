# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 00:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20160602_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Solo caracteres alfanumericos son permitidos.')], verbose_name='Nombre:'),
        ),
    ]
