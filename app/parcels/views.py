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

import parcels.models
import parcels.serializers

class HomeView(View):
    template = 'parcels/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        parcel = parcels.models.Dataset.objects.all()
        return render_to_response(self.template, {'parcel': parcel})


class ParcelView(View):
    template = 'parcels/parcel.html'

    def __str__(self):
        return 'ParcelView'

    def get(self, request, guid):
        parcel = get_object_or_404(parcels.models.Parcel, pk=guid)
        return render_to_response(self.template, {'parcel': parcel})

