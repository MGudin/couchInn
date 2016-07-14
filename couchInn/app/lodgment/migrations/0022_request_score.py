# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 22:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0021_remove_place_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='score',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
    ]
