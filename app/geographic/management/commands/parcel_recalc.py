#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
from core.utils import md5
import geographic.models


class Command(BaseCommand):
    help = 'Recalculates parcel distances.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--prefix',
            dest='prefix',
            default=False,
            help='Prefix to match against GUIDs.',
        )


    def handle(self, *args, **options):
        print('Processing parcels...')
        prefix = options['prefix']

        if prefix:
            i = 0
            parcels = geographic.models.Parcel.objects.filter(pk__startswith=prefix)
            p_count = parcels.count()
            for this_parcel in parcels:
                print(this_parcel)
                changed = this_parcel.recalc()
                if changed:
                    this_parcel.save()
                print('{}:{}'.format(i, p_count))
                i+=1
        else:
            i = 0
            parcels = geographic.models.Parcel.objects.all()
            p_count = parcels.count()
            for this_parcel in parcels:
                print(this_parcel)
                changed = this_parcel.recalc()
                if changed:
                    this_parcel.save()
                print('{}:{}'.format(i, p_count))
                i+=1