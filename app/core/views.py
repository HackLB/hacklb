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

import core.models
import core.serializers


class HomeView(View):
    template = 'core/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        # bodies = core.models.Body.objects.all().prefetch_related('meetings')
        # documents = core.models.Document.objects.all()
        return render_to_response(self.template)


class CustomSearchView(SearchView):
    """Custom search view."""

    template_name = 'search/search_bootstrap.html'
    form_class = SearchForm

    # def get_queryset(self):
    #     queryset = super(CustomSearchView, self).get_queryset()
    #     print(queryset.filter(content='honda').count())
    #     # further filter queryset based on some set of criteria
    #     return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(CustomSearchView, self).get_context_data(*args, **kwargs)
        # pprint(context)
        pprint(context['paginator'].count)
        # pprint(context['paginator'])
        # pprint(dir(context['page_obj']))
        # do something
        return context


# Now create your own that subclasses the base view
class CustomFacetedSearchView(FacetedSearchView):
    form_class = FacetedSearchForm
    facet_fields = ['component', 'manufacturer', 'model', 'year', ]
    template_name = 'search/search_bootstrap_facets.html'
    context_object_name = 'page_object'

