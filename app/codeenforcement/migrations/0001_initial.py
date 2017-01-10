# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 05:48
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime_updated', models.DateTimeField(auto_now=True, db_index=True, help_text='The datetime this actual object was updated.', null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The datetime this actual object was created.', null=True)),
                ('title', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_url', models.TextField(blank=True, null=True)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('geojson', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('file', models.FileField(blank=True, max_length=1024, null=True, upload_to='geographic')),
            ],
            options={
                'get_latest_by': '-datetime_updated',
                'abstract': False,
            },
        ),
    ]