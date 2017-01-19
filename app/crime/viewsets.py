from django.contrib.auth.models import User, Group
from rest_framework import viewsets, pagination
import crime.models
import crime.serializers
from rest_framework import permissions

class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = crime.models.Incident.objects.all()
    serializer_class = crime.serializers.IncidentSerializer


class IncidentGeoPagination(pagination.PageNumberPagination):       
    page_size = 100000


class IncidentGeoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = crime.models.Incident.objects.filter(magnitude__gte=0.7)
    serializer_class = crime.serializers.IncidentSpatialDataSerializerMagnitude
    pagination_class = IncidentGeoPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]