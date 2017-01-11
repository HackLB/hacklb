#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
import business.models
from core.utils import md5

class Command(BaseCommand):
    help = 'Updates business licenses.'


    def handle(self, *args, **options):

        for license in business.models.License.objects.all():
            license.save()
