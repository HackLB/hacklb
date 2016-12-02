from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import legistar.models
import legistar.serializers


class BodyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = legistar.models.Body.objects.all()
    serializer_class = legistar.serializers.BodySerializer



class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = legistar.models.Document.objects.all()
    serializer_class = legistar.serializers.DocumentSerializer



class MeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meetings to be viewed or edited.
    """
    queryset = legistar.models.Meeting.objects.all()
    serializer_class = legistar.serializers.MeetingSerializer


class AgendaItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows meeting Agenda Items to be viewed or edited.
    """
    queryset = legistar.models.AgendaItem.objects.all()
    serializer_class = legistar.serializers.AgendaItemSerializer
