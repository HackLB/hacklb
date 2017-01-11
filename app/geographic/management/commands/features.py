#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
import django.apps
from django.core.files import File
import os
from pprint import pprint
import simplejson as json
from core.utils import md5
import geographic.models
import requests


all_features = [{'type':'Dog Park', 'url':'http://datalb.longbeach.gov/datasets/cd799f269e604b2faa071b2715d154ee_18.geojson', 'prefix': 'dogpark'},
            {'type':'Government Buildings', 'url':'http://datalb.longbeach.gov/datasets/03bbfb09b9d147959dc4daaea9dd2b41_7.geojson', 'prefix': 'govbldg'},
            {'type': 'Council Offices', 'url': 'http://datalb.longbeach.gov/datasets/8fa1581536504ca29d12862333a5fa12_10.geojson', 'prefix': 'cdoff'},
            {'type': 'Recycle Centers', 'url': 'http://datalb.longbeach.gov/datasets/9f0034cc8fc248df8aff750810fd615a_21.geojson', 'prefix': 'recyc'},
            {'type': 'Utility Pay Stations', 'url': 'http://datalb.longbeach.gov/datasets/5917010f84f54c90a906bec24fcfbb35_11.geojson', 'prefix': 'utilpay'},
            {'type': 'Colleges', 'url': 'http://datalb.longbeach.gov/datasets/53c61ab2968b4706b959488e7cc337c5_2.geojson', 'prefix': 'college'},
            {'type': 'Post Offices', 'url': 'http://datalb.longbeach.gov/datasets/72c4a06e44e648c5a086e17a0a4e3790_12.geojson', 'prefix': 'postal'},
            {'type': 'Libraries', 'url': 'http://datalb.longbeach.gov/datasets/e2c20bf123bb4ae6b35f60afb2b244f1_4.geojson', 'prefix': 'library'},
            {'type': 'Parks', 'url': 'http://datalb.longbeach.gov/datasets/0a97b81583e8486eb5ad55d68287b7fb_17.geojson', 'prefix': 'park'},
            {'type': 'Public Refuse Container Locations', 'url': 'http://datalb.longbeach.gov/datasets/2a17471effa944f39c1b55af4b1946fe_0.geojson', 'prefix': 'trash'},
            {'type': 'Housing & Health Services', 'url': 'http://datalb.longbeach.gov/datasets/7ba8a844d3cb4c23853ba6b084250f4d_8.geojson', 'prefix': 'hhs'},
            {'type': 'Fire Stations', 'url': 'http://datalb.longbeach.gov/datasets/33bd87d486074834b70964459e20eb87_5.geojson', 'prefix': 'lbfd'},
            {'type': 'Police Stations', 'url': 'http://datalb.longbeach.gov/datasets/becc7c4243be46deb497b232d4bc92b4_6.geojson', 'prefix': 'lbpd'},
            {'type': 'Municipal Golf Courses', 'url': 'http://datalb.longbeach.gov/datasets/02d9e8c0f5f74f3eb4d4f654e7fff164_16.geojson', 'prefix': 'golf'},
            {'type': 'Animal Care and Adoptions', 'url': 'http://datalb.longbeach.gov/datasets/d7933a4f85ca4f31adb29594de4c0f38_15.geojson', 'prefix': 'spca'},
            {'type': 'Hospitals', 'url': 'http://datalb.longbeach.gov/datasets/fd14308f61dc40589c678fa4cf8116cb_1.geojson', 'prefix': 'hosp'},
            {'type': 'Metro Stations', 'url': 'http://datalb.longbeach.gov/datasets/37aa1580fe044bd5bd8ee9f7242f91a8_0.geojson', 'prefix': 'metro'},
            {'type': 'Skate Parks', 'url': 'http://datalb.longbeach.gov/datasets/e2a800374c0e42e9a5d6654f5037d377_20.geojson', 'prefix': 'skate'},
            {'type': 'Bike Facilities', 'url': 'http://datalb.longbeach.gov/datasets/167bb084757842daa22a56023759c995_14.geojson', 'prefix': 'bike'},
            {'type': 'Schools', 'url': 'http://datalb.longbeach.gov/datasets/27e03c3c885a478f97c1f0cae5a4728f_3.geojson', 'prefix': 'school'},
            {'type': 'Points of Interest', 'url': 'http://datalb.longbeach.gov/datasets/0ee57de4740e4363b79336addf491a7b_13.geojson', 'prefix': 'poi'}]


def ingest(feature):
    print(feature)

    r = requests.get(feature['url'])
    r_json = r.json()

    for json_feature in r_json['features']:

        if 'OBJECTID' in json_feature['properties']:
            obj_id = json_feature['properties']['OBJECTID']
        elif 'ObjectID' in json_feature['properties']:
            obj_id = json_feature['properties']['ObjectID']

        feature_id = '{}-{}'.format(feature['prefix'], obj_id)

        feature_record, created = geographic.models.Feature.objects.get_or_create(feature_id=feature_id, defaults={'json': json_feature, 'feature_type': feature['prefix']})
        print(feature_record)



class Command(BaseCommand):
    help = 'Ingests features from API.'


    def handle(self, *args, **options):
        # print('Processing {}...'.format(options['path']))

        for feature in all_features:
            ingest(feature)
