# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographic', '0008_auto_20170111_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='dist_trash',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
    ]