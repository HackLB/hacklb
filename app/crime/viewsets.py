from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import crime.models
import crime.serializers


class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = crime.models.Incident.objects.all()
    serializer_class = crime.serializers.IncidentSerializer
