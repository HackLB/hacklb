from rest_framework import serializers
import crime.search_indexes
import crime.models

from rest_framework_gis.serializers import GeoFeatureModelSerializer

class IncidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = crime.models.Incident
        exclude = ('json', )
        # fields = '__all__'



class IncidentSpatialDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = crime.models.Incident
        geo_field = 'coordinates'
        # fields = ('name', 'description', )
        exclude = ('json', )


class IncidentSpatialDataSerializerMagnitude(GeoFeatureModelSerializer):
    class Meta:
        model = crime.models.Incident
        geo_field = 'coordinates'
        fields = ('magnitude', )