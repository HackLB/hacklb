from rest_framework import serializers
import crime.search_indexes
import crime.models


class IncidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = crime.models.Incident
        exclude = ('json', )
        # fields = '__all__'

