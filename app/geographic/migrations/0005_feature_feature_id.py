# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographic', '0004_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='feature_id',
            field=models.TextField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
