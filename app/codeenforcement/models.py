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
# GIS classes
# --------------------------------------------------

class Dataset(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    A GIS dataset in GeoJSON format.

    """

    file = models.FileField(upload_to='geographic', null=True, blank=True, max_length=1024, )
    filename = models.TextField(null=True, blank=True, db_index=True, )

    def __str__(self):
        return '{} map'.format(self.file.name)

    def get_absolute_url(self):
        return reverse('geographic_dataset_details', args=[str(self.pk)])
        


# @receiver(pre_save, sender=Dataset)
# def dataset_filename(sender, instance, *args, **kwargs):
#     """
#     Creates a Metadata instance whenever an Asset is added, and
#     then extracts the metadata and populates the Metadata instance
#     """
#     if instance.file:
#         print('saving filename...')
#         instance.coordinates = 'POINT({} {})'.format(lon, lat)


# @receiver(pre_save, sender=Incident)
# def incident_metadata(sender, instance, *args, **kwargs):
#     """
#     Creates a Metadata instance whenever an Asset is added, and
#     then extracts th metadata and populates the Metadata instance
#     """
#     if instance.json:
#         instance.address = instance.json.get('block_address')
#         instance.case_number = instance.json.get('case_number')
#         instance.city = instance.json.get('city')
#         instance.state = instance.json.get('state')
#         instance.description = instance.json.get('description')
#         instance.title = instance.json.get('title')
#         instance.incident_id = instance.json.get('incident_id')

#         datetime_str = instance.json.get('date_occured')
#         if datetime_str:
#             instance.date_occured = arrow.get(datetime_str).datetime
