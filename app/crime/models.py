import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from haystack.utils.geo import Point
from core.models import GenericBaseClass, DescriptiveBaseClass, InternetResourceClass

# --------------------------------------------------
# Crime classes
# --------------------------------------------------

class Incident(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass):
    """
    A unique crime incident.
    """

    def __str__(self):
        return 'crime {}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('incident_details', args=[str(self.pk)])
        