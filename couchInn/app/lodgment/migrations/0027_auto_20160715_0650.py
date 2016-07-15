# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0026_auto_20160715_0641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='is_score',
            new_name='host_scored',
        ),
        migrations.AddField(
            model_name='request',
            name='tenant_scored',
            field=models.BooleanField(default=False),
        ),
    ]
