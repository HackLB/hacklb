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

# --------------------------------------------------
# Abstract base classes
# --------------------------------------------------

class GenericBaseClass(models.Model):
    """
    The standard abstract base class for primary classes provides basic fields and infrastructure for
    all Model classes in this project
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime_updated = models.DateTimeField(auto_now=True, null=True, blank=True, db_index = True, help_text='The datetime this actual object was updated.', )
    datetime_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index = True, help_text='The datetime this actual object was created.', )


    class Meta:
        abstract = True
        get_latest_by = '-datetime_updated'


class DescriptiveBaseClass(models.Model):
    """
    A descriptive abstract base class for primary classes provides basic descriptive fields, 
    a la Dublin Core, for concrete classes to use as a mixin.
    """
    name = models.CharField(null=True, blank=True, db_index=True, max_length=256, )
    description = models.TextField(null=True, blank=True, )

    class Meta:
        abstract = True


class InternetResourceClass(models.Model):
    """
    A descriptive abstract base class for primary classes provides basic descriptive fields, 
    a la Dublin Core, for concrete classes to use as a mixin.
    """
    source_url = models.TextField(null=True, blank=True, )
    json = JSONField(null=True, blank=True, )

    class Meta:
        abstract = True

