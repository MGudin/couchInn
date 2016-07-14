# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0007_auto_20160614_0446'),
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='session.CouchinnUser'),
            preserve_default=False,
        ),
    ]