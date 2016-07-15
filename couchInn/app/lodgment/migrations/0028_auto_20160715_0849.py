# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 08:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0027_auto_20160715_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='score',
        ),
        migrations.AddField(
            model_name='request',
            name='host_score',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
        migrations.AddField(
            model_name='request',
            name='tenant_score',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
    ]
