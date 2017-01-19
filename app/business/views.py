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

import business.models
import random


def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))


class HomeView(View):
    template = 'geographic/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        return render_to_response(self.template)






# main_template = { "labels": [], "datasets": []}

# district_template = {"label": "District 1", "data": [65, 59, 80, 81, 56, 55, 40], "spanGaps": False}

class StatsByDistrictView(View):

    # colors = [random_color() for x in range(9)]

    def __str__(self):
        return 'StatsByDistrictView'


    def get(self, request):
        years = range(1980, 2017)
        districts = range(1, 10)

        data = {"labels": [str(x) for x in years], "datasets": []}

        for district in districts:

            color = random_color()

            year_counts = [business.models.License.objects.filter(district=district).filter(license_year=str(year)).count() for year in years]

            district_data = {"fill": False, "lineTension": 0.1, "backgroundColor": "rgba({},{},{},0.4)".format(*color), "borderColor": "rgba({},{},{},1)".format(*color), "borderCapStyle": 'butt', "borderDash": [], "borderDashOffset": 0.0, "borderJoinStyle": 'miter', "pointBorderColor": "rgba({},{},{},1)".format(*color), "pointBackgroundColor": "#fff", "pointBorderWidth": 1, "pointHoverRadius": 5, "pointHoverBackgroundColor": "rgba({},{},{},1)".format(*color), "pointHoverBorderColor": "rgba(220,220,220,1)", "pointHoverBorderWidth": 2, "pointRadius": 1, "pointHitRadius": 10, "spanGaps": False,}

            district_data["label"] = "District {}".format(district)
            district_data["data"] = year_counts

            data['datasets'].append(district_data)

        # recs = business.models.License.objects.filter(business_category__contains='Restaurant')


        return JsonResponse(data)


class DatasetView(View):
    template = 'geographic/dataset.html'

    def __str__(self):
        return 'DatasetView'

    def get(self, request, guid):
        dataset = get_object_or_404(geographic.models.Dataset, pk=guid)
        return render_to_response(self.template, {'dataset': dataset})

