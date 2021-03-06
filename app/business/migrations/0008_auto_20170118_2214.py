# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_license_home_based'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='business_type',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='class_description',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='company_type',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='inactive_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='iss_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='license_type',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='nonprofit',
            field=models.NullBooleanField(db_index=True),
        ),
        migrations.AddField(
            model_name='license',
            name='product_types',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='property_type',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='license',
            name='seats',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
