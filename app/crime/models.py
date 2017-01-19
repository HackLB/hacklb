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
# Crime classes
# --------------------------------------------------

class Incident(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    A unique crime incident.

    {
        "block_address": "CEDAR AV & W 14TH ST N",
        "case_number": 150060006,
        "city": "Long Beach",
        "date_occured": "2015-09-28 17:24:00 UTC",
        "description": null,
        "incident_id": 100,
        "latitude": 33.7836946,
        "longitude": -118.1950572,
        "state": "CA",
        "title": "BURGLARY - RESIDENTIAL"
    }

    """

    case_number = models.IntegerField(null=True, blank=True, db_index = True, )
    description = models.TextField(null=True, blank=True, db_index = True, )
    date_occured = models.DateTimeField(null=True, blank=True, db_index = True, help_text='The date and time of the incident.', )
    incident_id = models.IntegerField(null=True, blank=True, db_index = True, )
    address = models.TextField(null=True, blank=True, db_index = True, )
    city = models.TextField(null=True, blank=True, db_index = True, )
    state = models.TextField(null=True, blank=True, db_index = True, )
    magnitude = models.FloatField(null=True, blank=True, db_index = True, )

    def __str__(self):
        return '{}, {} on {} ({})'.format(self.title, self.address, self.date_occured, self.pk)

    def get_absolute_url(self):
        return reverse('crime_incident_details', args=[str(self.pk)])
        

    @property
    def magnitude_calc(self):
        mag = 0.2
        crime = self.title

        if 'UNREASONABLE NOISE' in crime:
            mag = 0.3

        if 'PETTY THEFT' in crime or 'VANDALISM' in crime:
            mag = 0.4

        if 'ROBBERY; COMMERCIAL' in crime or 'GRAND THEFT' in crime or 'FRAUD' in crime or 'HIT AND RUN WITHOUT INJURY' in crime or 'UNAUTHORIZED USE' in crime or 'FORGERY' in crime:
            mag = 0.6

        if 'ROBBERY; PERSON' in crime or 'BURGLARY' in crime or 'HIT AND RUN WITH INJURY' in crime:
            mag = 0.7

        if 'ASSAULT' in crime or 'BATTERY' in crime or 'VIOLENCE' in crime or 'FIGHT' in crime or 'WITH FIREARM' in crime or 'INFLICT CORP INJURY' in crime or 'DEADLY WEAPON' in crime or 'DOMESTIC VIOLENCE' in crime:
            mag = 0.8

        if 'RAPE' in crime or 'KIDNAPPING' in crime:
            mag = 0.9

        if 'MURDER' in crime:
            mag = 1.0

        return mag

@receiver(pre_save, sender=Incident)
def incident_location(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts the metadata and populates the Metadata instance
    """
    if instance.json and ('latitude' in instance.json) and ('longitude' in instance.json) and (not instance.coordinates):
        instance.coordinates = Point(instance.json['longitude'], instance.json['latitude'])
        print('saving coordinates...')


@receiver(pre_save, sender=Incident)
def incident_metadata(sender, instance, *args, **kwargs):
    """
    Creates a Metadata instance whenever an Asset is added, and
    then extracts th metadata and populates the Metadata instance
    """
    if instance.json:
        instance.address = instance.json.get('block_address')
        instance.case_number = instance.json.get('case_number')
        instance.city = instance.json.get('city')
        instance.state = instance.json.get('state')
        instance.description = instance.json.get('description')
        instance.title = instance.json.get('title')
        instance.incident_id = instance.json.get('incident_id')

        datetime_str = instance.json.get('date_occured')
        if datetime_str:
            instance.date_occured = arrow.get(datetime_str).datetime
