# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20170111_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_status',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]