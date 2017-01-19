#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
from core.utils import md5
import geographic.models


def ingest(path):
    print(path)

    if path.endswith('.geojson'):
        with open(path) as f:
            data = json.load(f)

        for this_feature in data['features']:
            route_obj, created = geographic.models.Route.objects.get_or_create(objectid=this_feature['properties']['OBJECTID'], defaults={'json': this_feature, 'route_type': 'bikeway'})


class Command(BaseCommand):
    help = 'Upserts routes from a GeoJSON file.'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        print('Processing {}...'.format(options['path']))

        ingest(options['path'])
