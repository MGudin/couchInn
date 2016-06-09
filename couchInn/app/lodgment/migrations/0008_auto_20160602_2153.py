# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 21:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lodgment', '0007_auto_20160602_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Nombre')),
                ('direction', models.TextField(max_length=100, verbose_name='Direcci\xf3n')),
                ('city', models.TextField(max_length=100, verbose_name='Ciudad')),
                ('province', models.TextField(max_length=100, verbose_name='Provincia')),
                ('score', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lodgment',
            name='description',
            field=models.TextField(default=None, max_length=500, verbose_name='Descripci\xf3n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lodgment',
            name='reservations_available',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de personas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lodgment',
            name='score',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Valoraci\xf3n'),
        ),
        migrations.AddField(
            model_name='lodgment',
            name='place',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lodgment.Place'),
            preserve_default=False,
        ),
    ]