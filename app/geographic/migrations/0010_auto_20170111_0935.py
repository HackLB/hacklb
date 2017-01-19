# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 09:35
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geographic', '0009_parcel_dist_trash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, db_index=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='feature',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, db_index=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, db_index=True, null=True, srid=4326),
        ),
    ]
