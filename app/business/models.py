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
    iss_datetime = models.DateTimeField(null=True, blank=True, db_index=True, )

    license_number = models.TextField(null=True, blank=True, db_index=True, unique=True, )
    license_type = models.TextField(null=True, blank=True, db_index=True, )
    license_status = models.TextField(null=True, blank=True, db_index=True, )
    license_active = models.NullBooleanField(null=True, blank=True, db_index=True, )
    license_datetime = models.DateTimeField(null=True, blank=True, db_index=True, )
    license_year = models.TextField(null=True, blank=True, db_index=True, )

    inactive_datetime = models.DateTimeField(null=True, blank=True, db_index=True, )

    milestone = models.TextField(null=True, blank=True, db_index=True, )
    milestone_datetime = models.DateTimeField(null=True, blank=True, db_index=True, )

    class_description = models.TextField(null=True, blank=True, db_index=True, )
    company_type = models.TextField(null=True, blank=True, db_index=True, )

    business_category = models.TextField(null=True, blank=True, db_index=True, )
    business_type = models.TextField(null=True, blank=True, db_index=True, )
    business_class = models.TextField(null=True, blank=True, db_index=True, )
    dba = models.TextField(null=True, blank=True, db_index=True, )
    employees = models.IntegerField(null=True, blank=True, db_index=True, )
    seats = models.IntegerField(null=True, blank=True, db_index=True, )

    location = models.TextField(null=True, blank=True, db_index=True, )
    zip_code = models.TextField(null=True, blank=True, db_index=True, )
    property_type = models.TextField(null=True, blank=True, db_index=True, )
    product_types = models.TextField(null=True, blank=True, db_index=True, )
    district = models.IntegerField(null=True, blank=True, db_index=True, )

    home_based = models.NullBooleanField(null=True, blank=True, db_index=True, )
    nonprofit = models.NullBooleanField(null=True, blank=True, db_index=True, )

    def __str__(self):
        return 'license: {}'.format(self.license_number)

    def get_absolute_url(self):
        return reverse('business_license_details', args=[str(self.pk)])


#     "properties": {
#         "LICENSENO": "BU20010360",
#         "NONPROFIT": null,
#         "NUMBOOTHS": null,
#         "NUMSEATS": 0,
#         "NUMSELLINGDAYS": null,
#         "NUMSTANDS": 0,
#         "NUMUNITS": 0,
#         "NUMVEH": 0,
#     },
#     "type": "Feature"
# }


@receiver(pre_save, sender=License)
def license_metadata(sender, instance, *args, **kwargs):
    """
    Extracts and sets various instance properties based on JSON metadata.
    """
    if instance.json and 'properties' in instance.json:
        instance.title = instance.json['properties'].get('FULLNAME')

        instance.class_description = instance.json['properties'].get('CLASSDESC')
        instance.company_type = instance.json['properties'].get('COMPANYTYPE')

        instance.license_status = instance.json['properties'].get('LICSTATUS')
        instance.license_type = instance.json['properties'].get('LICENSETYPE')

        iss_datestr = instance.json['properties'].get('ISSDTTM')
        if iss_datestr:
            instance.iss_datetime = arrow.get(iss_datestr).datetime

        inactive_datestr = instance.json['properties'].get('INACTVDTTM')
        if inactive_datestr:
            instance.inactive_datetime = arrow.get(inactive_datestr).datetime

        license_datestr = instance.json['properties'].get('LICENSEDTTM')
        if license_datestr:
            instance.license_datetime = arrow.get(license_datestr).datetime

        instance.license_year = instance.license_datetime.year

        instance.milestone = instance.json['properties'].get('MILESTONE')
        milestone_datestr = instance.json['properties'].get('MILESTONEDATE')
        if milestone_datestr:
            instance.milestone_datetime = arrow.get(milestone_datestr).datetime

        instance.business_category = instance.json['properties'].get('LICCATDESC')
        instance.business_type = instance.json['properties'].get('TYPEOFBUSINESS')
        instance.business_class = instance.json['properties'].get('CLASSDESC')

        instance.dba = instance.json['properties'].get('DBANAME')
        instance.employees = int(instance.json.get('properties').get('NUMEMP', 0))
        instance.seats = int(instance.json.get('properties').get('NUMSEATS', 0))

        instance.location = instance.json['properties'].get('SITELOCATION')
        instance.zip_code = instance.json['properties'].get('ZIP')
        instance.property_type = instance.json['properties'].get('PROPERTYTYPE')
        instance.product_types = instance.json['properties'].get('PRODUCTTYPES')
        instance.district = int(instance.json.get('properties').get('COUNCILDISTRICT', 0))

        home_biz = instance.json['properties'].get('HOMEBASED')
        if home_biz =='Yes':
            instance.home_based = True
        elif home_biz =='No':
            instance.home_based = False

        non_profit = instance.json['properties'].get('NONPROFIT')
        if non_profit =='Yes':
            instance.nonprofit = True
        elif non_profit =='No':
            instance.nonprofit = False

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