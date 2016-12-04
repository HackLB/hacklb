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

import geographic.models
import geographic.serializers

class HomeView(View):
    template = 'geographic/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        datasets = geographic.models.Dataset.objects.all()
        return render_to_response(self.template, {'datasets': datasets})


class DatasetView(View):
    template = 'geographic/dataset.html'

    def __str__(self):
        return 'DatasetView'

    def get(self, request, guid):
        dataset = get_object_or_404(geographic.models.Dataset, pk=guid)
        return render_to_response(self.template, {'dataset': dataset})

