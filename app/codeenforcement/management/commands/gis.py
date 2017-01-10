#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
import os
from pprint import pprint
import simplejson as json
import crime.models

class Command(BaseCommand):
    help = 'Upserts crime incidents.'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        print(options['path'])

        for directory, directories, files in os.walk(options['path'], topdown=False):
            for name in files:
                path = os.path.join(directory, name)
                if name.endswith('.json'):
                    pprint(path)

                    with open(path) as f:
                        data = json.load(f)
                        pprint(data)

                        body, created = crime.models.Incident.objects.get_or_create(case_number=data.get('case_number'), defaults={'json': data})