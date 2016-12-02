import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from PIL import Image
from core.utils.pdf import PDF
from haystack.utils.geo import Point
from core.models import GenericBaseClass, DescriptiveBaseClass, InternetResourceClass

# --------------------------------------------------
# HackLB classes
# --------------------------------------------------

class Document(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    A unique public document.
    """

    original = models.FileField(upload_to='legistar', null=True, blank=True, max_length=1024, )
    md5 = models.CharField(null=True, blank=True, db_index=True, max_length=64, )
    meeting = models.ForeignKey('Meeting', related_name='documents', null=True, blank=True, )
    agenda_item = models.ForeignKey('AgendaItem', related_name='attachments', null=True, blank=True, )

    text = models.TextField(null=True, blank=True, )

    def __str__(self):
        if self.original:
            return '/'.join(self.original.url.split('/')[-2:])
        else:
            return 'unnamed document'

    def get_absolute_url(self):
        return reverse('document_details', args=[str(self.pk)])


@receiver(pre_save, sender=Document)
def document_text(sender, instance, *args, **kwargs):
    """
    Extracts text from PDFs on save.
    """
    if instance.original and not instance.text and instance.original.path.endswith('.pdf'):
        print('Extracting text from {}...'.format(instance.pk))
        pdf = PDF(instance.original.path)
        if pdf:
            instance.text = pdf.text
    else:
        print('Skipping extraction from {}...'.format(instance.pk))


class Meeting(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    A public meeting.
    """

    body = models.ForeignKey('Body', related_name='meetings', )
    guid = models.CharField(max_length=64, db_index=True, )

    location = models.TextField(null=True, blank=True, )
    coordinates = models.PointField(null=True, blank=True,)
    time = models.DateTimeField(null=True, blank=True, db_index = True, )

    def __str__(self):
        if self.name:
            return '{}, {}'.format(self.name, self.time)
        else:
            return 'meeting: {}'.format(self.guid)

    def get_absolute_url(self):
        return reverse('meeting_details', args=[str(self.pk)])


class Body(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    A public body, such as a commission or sub-committee.
    """

    slug = models.CharField(max_length=1024, db_index=True, unique=True, )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.slug

    def get_absolute_url(self):
        return reverse('body_details', args=[str(self.pk)])


class AgendaItem(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    An agenda item for a meeting.
    """

    name = models.CharField(max_length=256, db_index=True, )
    description = models.TextField(null=True, blank=True, )
    number = models.IntegerField(db_index=True, null=True, blank=True, )
    version = models.IntegerField(db_index=True, )
    meeting = models.ForeignKey('Meeting', related_name='agenda_items', null=True, blank=True, )
    type = models.CharField(max_length=256, db_index=True, null=True, blank=True, )

    def __str__(self):
        return '{}: {}'.format(self.number, self.name)

    def get_absolute_url(self):
        return reverse('agendaitem_details', args=[str(self.pk)])



@receiver(pre_save, sender=Meeting)
def meeting_location(sender, instance, *args, **kwargs):
    """
    Set geofield to value from GeoJSON if it exists.
    """
    if instance.json and ('coordinates' in instance.json) and (not instance.coordinates):
        print('saving coordinates...')
        lat = instance.json['coordinates']['latitude']
        lon = instance.json['coordinates']['longitude']
        instance.coordinates = 'POINT({} {})'.format(lon, lat)

    if instance.json and ('coordinates' in instance.json) and (not instance.location):
        print('saving location...')
        instance.location = instance.json['coordinates']['address']



@receiver(post_save, sender=Meeting)
def meeting_json(sender, instance, created, **kwargs):
    """
    Sets name and time of meeting from JSON if it exists.
    """
    if created and instance.json:
        print('new meeting, json processing')
        instance.name = instance.json['name']

        parsed_datetime = parse_datetime(instance.json['datetime'])
        if not is_aware(parsed_datetime):
            parsed_datetime = make_aware(parsed_datetime)
        instance.time = parsed_datetime

        instance.source_url = instance.json['link']

        instance.save()
        