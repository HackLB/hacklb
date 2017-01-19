from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.models import User, Group
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from haystack.generic_views import SearchView, FacetedSearchView
from haystack.forms import SearchForm, ModelSearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet

import crime.models
import crime.serializers


class HomeView(View):
    template = 'crime/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        incidents = crime.models.Incident.objects.all()
        return render_to_response(self.template, {'incidents': incidents})


class IncidentView(View):
    template = 'crime/incident.html'

    def __str__(self):
        return 'IncidentView'

    def get(self, request, guid):
        incident = get_object_or_404(crime.model.Incident, pk=guid)
        return render_to_response(self.template, {'incident': incident})



class IncidentGeoJSON(View):
    # template = 'crime/incident.html'

    geojson_template = {"type": "FeatureCollection", "features": []}

    


    def __str__(self):
        return 'IncidentGeoJSON'

    def get(self, request, guid):

        gj = geojson_template

        # incident_template = {"type": "Feature", "geometry": {}, "properties": {}}

        incidents = crime.models.Incident.objects.all()[0:1000]
        for incident in incidents:
            feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [incident.json['longitude'], incident.json['latitude']]}, "properties": {'mag': incident.magnitude }}
            gj['features'].append(feature)

        return JsonResponse(gj)

