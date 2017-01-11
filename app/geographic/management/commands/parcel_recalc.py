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

    def handle(self, *args, **options):
        print('Processing parcels...')

        for this_parcel in geographic.models.Parcel.objects.all():
            print(this_parcel)
            this_parcel.recalc()
            this_parcel.save()