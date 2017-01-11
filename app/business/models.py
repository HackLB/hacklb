import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from haystack.utils.geo import Point
from core.models import GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass
import arrow

# --------------------------------------------------
# Business License classes
# --------------------------------------------------

class License(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    A GIS dataset in GeoJSON format.
    """

    license_number = models.TextField(null=True, blank=True, db_index=True, unique=True, )
    license_status = models.TextField(null=True, blank=True, db_index=True, )
    license_datetime = models.DateTimeField(null=True, blank=True, db_index=True, )

    business_category = models.TextField(null=True, blank=True, db_index=True, )
    business_class = models.TextField(null=True, blank=True, db_index=True, )
    dba = models.TextField(null=True, blank=True, db_index=True, )
    employees = models.IntegerField(null=True, blank=True, db_index=True, )

    location = models.TextField(null=True, blank=True, db_index=True, )
    zip_code = models.TextField(null=True, blank=True, db_index=True, )

    def __str__(self):
        return 'license: {}'.format(self.license_number)

    def get_absolute_url(self):
        return reverse('business_license_details', args=[str(self.pk)])



@receiver(pre_save, sender=License)
def license_metadata(sender, instance, *args, **kwargs):
    """
    Extracts and sets various instance properties based on JSON metadata.
    """
    if instance.json:
        instance.dba = instance.json.get('properties', []).get('DBANAME')
        instance.title = instance.json.get('properties', []).get('FULLNAME')

        instance.business_class = instance.json.get('properties', []).get('CLASSDESC')
        instance.business_category = instance.json.get('properties', []).get('LICCATDESC')
        instance.employees = int(instance.json.get('properties', []).get('NUMEMP'))

        instance.location = instance.json.get('properties', []).get('SITELOCATION')
        instance.zip_code = instance.json.get('properties', []).get('ZIP')

        instance.license_status = instance.json.get('properties', []).get('LICSTATUS')

        dt = instance.json.get('properties', []).get('LICENSEDTTM')
        instance.license_datetime = arrow.get(dt).datetime

        print('saving #{}...'.format(instance.pk))


@receiver(pre_save, sender=License)
def license_coordinates(sender, instance, *args, **kwargs):
    """
    Extracts and sets license.coordinates based on the centroid
    of a given polygon, or a single set of x,y coordinates.
    """
    if instance.json:
        coords = instance.json['geometry']['coordinates']

        if len(coords) == 2:
            instance.coordinates = Point(coords)
            print('point: {},{}'.format(instance.coordinates.x, instance.coordinates.y))