# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 21:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20160623_1922'),
        ('lodgment', '0019_auto_20160623_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodgment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lodgment',
            name='category',
        ),
        migrations.RemoveField(
            model_name='lodgment',
            name='place',
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Couch', 'verbose_name_plural': 'Couchs'},
        ),
        migrations.RemoveField(
            model_name='request',
            name='lodgment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='lodgment',
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(default='as', max_length=500, verbose_name='Descripci\xf3n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='finish_date',
            field=models.DateField(default=None, verbose_name='Fecha de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='initial_date',
            field=models.DateField(default=None, verbose_name='Fecha de inicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='reservations_available',
            field=models.PositiveSmallIntegerField(default=None, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de personas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='title',
            field=models.CharField(default='sin titulo', max_length=50, verbose_name='Titulo'),
        ),
        migrations.AddField(
            model_name='request',
            name='couch',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lodgment.Place'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='couch',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lodgment.Place'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='score',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
        migrations.DeleteModel(
            name='Lodgment',
        ),
    ]