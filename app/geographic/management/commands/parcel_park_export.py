#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
import geographic.models


def export(path):
    print(path)

    all_features = {"type": "FeatureCollection", "features": []}

    for this_parcel in geographic.models.Parcel.objects.filter(dist_park__isnull=False):
        print(this_parcel)

        parcel_template = {"type": "Feature", "geometry": {}, "properties": {}}

        parcel_json = parcel_template
        parcel_json['geometry'] = this_parcel.json['geometry']
        parcel_json['properties'] = {}
        parcel_json['properties']['parksc'] = this_parcel.dist_park

        all_features['features'].append(parcel_json)

    with open(path, 'w') as f:
        json.dump(all_features, f, ensure_ascii=False)



class Command(BaseCommand):
    help = 'Upserts parcels from a GeoJSON file.'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        print('Processing {}...'.format(options['path']))

        export(options['path'])

