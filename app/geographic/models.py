import os, uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from haystack.utils.geo import Point
from django.contrib.gis.geos import Polygon, LineString
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from core.models import GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass
import arrow
from pprint import pprint

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
        



class Feature(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    Land parcels in the city of Long Beach.
    coordinates - the centroid of the given polygon
    """

    feature_type = models.TextField(null=True, blank=True, db_index=True, )
    feature_id = models.TextField(null=True, blank=True, db_index=True, unique=True, )
    location = models.TextField(null=True, blank=True, db_index=True, )
    telephone = models.TextField(null=True, blank=True, db_index=True, )

    def __str__(self):
        return '{}, {} ({})'.format(self.title, self.feature_type, self.feature_id)

    def get_absolute_url(self):
        return reverse('feature_details', args=[str(self.pk)])
        


@receiver(pre_save, sender=Feature)
def feature_metadata(sender, instance, *args, **kwargs):
    """
    Extracts and sets various instance properties based on JSON metadata.
    """
    if instance.json:
        instance.title = instance.json.get('properties', {}).get('NAME')
        instance.location = instance.json.get('properties', {}).get('ADDRESS')
        instance.telephone = instance.json.get('properties', {}).get('TELEPHONE')

        # print('saving feature {}...'.format(instance.pk))


@receiver(pre_save, sender=Feature)
def feature_coordinates(sender, instance, *args, **kwargs):
    """
    Extracts and sets license.coordinates based on the centroid
    of a given polygon, or a single set of x,y coordinates.
    """
    if instance.json:
        try:
            coords = instance.json['geometry']['coordinates']
            if len(coords) == 2:
                instance.coordinates = Point(coords)
                # print('point: {},{}'.format(instance.coordinates.x, instance.coordinates.y))
        except:
            pass



class Route(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    Land parcels in the city of Long Beach.
    coordinates - the centroid of the given polygon
    """

    objectid = models.IntegerField(null=True, blank=True, db_index=True, )
    linestring = models.LineStringField(null=True, blank=True, db_index=False, )
    route_type = models.TextField(null=True, blank=True, db_index=True, )


    def __str__(self):
        return '{} ({})'.format(self.title, self.pk)

    def get_absolute_url(self):
        return reverse('route_details', args=[str(self.pk)])



@receiver(pre_save, sender=Route)
def route_metadata(sender, instance, *args, **kwargs):
    """
    Extracts and sets various instance properties based on JSON metadata.
    """
    if instance.json:
        props = instance.json['properties']
        instance.objectid = props.get('OBJECTID')
        instance.title = '{}, {}'.format(props.get('NAME'), props.get('LIMITS'))


@receiver(pre_save, sender=Route)
def route_coordinates(sender, instance, *args, **kwargs):
    """
    Extracts and sets parcel.coordinates based on the centroid
    of a given polygon, or a single set of x,y coordinates.
    """
    if instance.json:
        coords = instance.json['geometry']['coordinates']
        geo_type = instance.json['geometry']['type']

        if geo_type == 'LineString':
            try:
                instance.linestring = LineString(coords)
                instance.coordinates = instance.linestring.centroid
                # print('poly: {},{}'.format(instance.coordinates.x, instance.coordinates.y))
            except:
                pprint(instance.json)
        # elif geo_type == 'MultiPolygon':
        #     try:
        #         this_poly = Polygon(coords[0])
        #         this_centroid = this_poly.centroid
        #         instance.coordinates = this_centroid
        #         # print('multiply: {},{}'.format(instance.coordinates.x, instance.coordinates.y))
        #     except:
        #         pprint(instance.json)




class Parcel(GenericBaseClass, DescriptiveBaseClass, InternetResourceClass, PlaceBaseClass):
    """
    Land parcels in the city of Long Beach.
    coordinates - the centroid of the given polygon
    """

    objectid = models.IntegerField(null=True, blank=True, db_index=True, )
    polygon = models.PolygonField(null=True, blank=True, db_index=True,)

    dist_lbpd = models.FloatField(null=True, blank=True, db_index=True, )
    dist_park = models.FloatField(null=True, blank=True, db_index=True, )
    dist_trash = models.FloatField(null=True, blank=True, db_index=True, )
    dist_bike = models.FloatField(null=True, blank=True, db_index=True, )

    def __str__(self):
        return '{} parcel'.format(self.pk)

    def get_absolute_url(self):
        return reverse('parcel_details', args=[str(self.pk)])

    def recalc(self):
        changed = False

        if self.dist_lbpd == None:
            res = self.nearest('lbpd')
            if res:
                self.dist_lbpd = res.distance.m
                changed = True
                print('nearest lbpd to {} is {}, {}m away'.format(self, res, self.dist_lbpd))

        if self.dist_park == None:
            res = self.nearest('park')
            if res:
                self.dist_park = res.distance.m
                changed = True
                print('nearest park to {} is {}, {}m away'.format(self, res, self.dist_park))

        if self.dist_trash == None:
            res = self.nearest('trash')
            if res:
                self.dist_trash = res.distance.m
                changed = True
                print('nearest trash to {} is {}, {}m away'.format(self, res, self.dist_trash))

        if self.dist_bike == None:
            res = self.nearest('bikeway')
            if res:
                self.dist_bike = res.distance.m
                changed = True
                print('nearest bikeway to {} is {}, {}m away'.format(self, res, self.dist_trash))

        return changed

    def nearest(self, kind):
        if self.coordinates:
            if kind == 'bikeway':
                routes = Route.objects.filter(route_type=kind).annotate(distance=Distance('linestring', self.coordinates)).order_by('distance')
                if routes.count() > 0:
                    return routes.first()
            else:
                features = Feature.objects.filter(feature_type=kind).annotate(distance=Distance('coordinates', self.coordinates)).order_by('distance')
                if features.count() > 0:
                    return features.first()
        return None


@receiver(pre_save, sender=Parcel)
def parcel_coordinates(sender, instance, *args, **kwargs):
    """
    Extracts and sets parcel.coordinates based on the centroid
    of a given polygon, or a single set of x,y coordinates.
    """
    if instance.json:
        coords = instance.json['geometry']['coordinates'][0]
        geo_type = instance.json['geometry']['type']

        if geo_type == 'Polygon':
            try:
                this_poly = Polygon(coords)
                this_centroid = this_poly.centroid
                instance.coordinates = this_centroid
                # print('poly: {},{}'.format(instance.coordinates.x, instance.coordinates.y))
            except:
                pprint(instance.json)
        elif geo_type == 'MultiPolygon':
            try:
                this_poly = Polygon(coords[0])
                this_centroid = this_poly.centroid
                instance.coordinates = this_centroid
                # print('multiply: {},{}'.format(instance.coordinates.x, instance.coordinates.y))
            except:
                pprint(instance.json)




@receiver(pre_save, sender=Parcel)
def parcel_metadata(sender, instance, *args, **kwargs):
    """
    Extracts and sets various instance properties based on JSON metadata.
    """
    if instance.json:
        instance.objectid = instance.json['properties']['OBJECTID']
        # print('saving #{}...'.format(instance.objectid))
