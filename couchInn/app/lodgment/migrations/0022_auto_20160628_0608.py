# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0021_auto_20160628_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Couch',
            new_name='couch',
        ),
    ]
