from rest_framework import serializers
import geographic.search_indexes
import geographic.models


class DatasetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = geographic.models.Dataset
        exclude = ('json', )
        # fields = '__all__'

