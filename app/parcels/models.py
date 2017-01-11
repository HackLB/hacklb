import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from haystack.utils.geo import Point
from django.contrib.gis.geos import Polygon
from core.models import GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass
import arrow
from pprint import pprint

# --------------------------------------------------
# Feature classes
# --------------------------------------------------

class Parcel(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    A GIS dataset in GeoJSON format.

    """

    objectid = models.IntegerField(null=True, blank=True, db_index=True, )
    polygon = models.PolygonField(null=True, blank=True, db_index=True,)

    def __str__(self):
        return '{} parcel'.format(self.pk)

    def get_absolute_url(self):
        return reverse('parcel_details', args=[str(self.pk)])
        


# @receiver(pre_save, sender=Dataset)
# def dataset_filename(sender, instance, *args, **kwargs):
#     """
#     Creates a Metadata instance whenever an Asset is added, and
#     then extracts the metadata and populates the Metadata instance
#     """
#     if instance.file:
#         print('saving filename...')
#         instance.coordinates = 'POINT({} {})'.format(lon, lat)


@receiver(pre_save, sender=Parcel)
def parcel_polygon(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts th metadata and populates the Metadata instance
    """
    if instance.json:
        this_poly = Polygon(instance.json['geometry']['coordinates'][0])
        this_centroid = this_poly.centroid
        # pprint(this_poly.centroid)
        instance.coordinates = this_centroid


@receiver(pre_save, sender=Parcel)
def parcel_metadata(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts th metadata and populates the Metadata instance
    """
    if instance.json:
        instance.objectid = instance.json['properties']['OBJECTID']
        print('saving #{}...'.format(instance.objectid))
