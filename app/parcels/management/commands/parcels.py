#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
from core.utils import md5
import parcels.models

def ingest(path):
    print(path)

    if path.endswith('.geojson'):
        # pprint(path)

        with open(path) as f:
            data = json.load(f)

        for this_feature in data['features']:
            pprint(this_feature['geometry']['coordinates'][0])

            parcel, created = parcels.models.Parcel.objects.get_or_create(objectid=this_feature['properties']['OBJECTID'], defaults={'json': this_feature})

        # if created:
        #     dataset.file.save(name, File(open(path)))
        #     dataset.save()

class Command(BaseCommand):
    help = 'Upserts parcels.'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        # print(options['path'])

        ingest(options['path'])

        # for directory, directories, files in os.walk(options['path'], topdown=False):
        #     for name in files:
        #         path = os.path.join(directory, name)
        #         if name.endswith('.geojson'):
        #             # pprint(path)

        #             dataset, created = geographic.models.Dataset.objects.get_or_create(filename=name)

        #             if created:
        #                 dataset.file.save(name, File(open(path)))
        #                 dataset.save()