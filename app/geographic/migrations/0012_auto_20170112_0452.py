# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 04:52
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geographic', '0011_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='linestring',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326),
        ),
    ]
