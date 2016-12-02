from rest_framework import serializers
import legistar.search_indexes
import legistar.models


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = legistar.models.Document
        fields = '__all__'


class BodySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = legistar.models.Body
        fields = '__all__'


class MeetingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = legistar.models.Meeting
        fields = '__all__'


class AgendaItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = legistar.models.AgendaItem
        fields = '__all__'
