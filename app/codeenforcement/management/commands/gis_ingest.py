#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
import geographic.models
from core.utils import md5

class Command(BaseCommand):
    help = 'Upserts crime incidents.'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        print(options['path'])

        for directory, directories, files in os.walk(options['path'], topdown=False):
            for name in files:
                path = os.path.join(directory, name)
                if name.endswith('.geojson'):
                    # pprint(path)

                    dataset, created = geographic.models.Dataset.objects.get_or_create(filename=name)

                    if created:
                        dataset.file.save(name, File(open(path)))
                        dataset.save()