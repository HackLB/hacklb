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
    template = 'business/home.html'

    def __str__(self):
        return 'HomeView'

    def get(self, request):
        return render_to_response(self.template)



class LicensesByDistrictView(View):
    template = 'business/licenses_by_district.html'

    def __str__(self):
        return 'LicensesByDistrictView'

    def get(self, request):
        return render_to_response(self.template)


class LicensesByDistrictDataView(View):

    def __str__(self):
        return 'LicensesByDistrictDataView'

    def get(self, request):
        years = range(1980, 2017)
        districts = range(1, 10)

        data = {"labels": [str(x) for x in years], "datasets": []}

        colors = [ (0, 51, 204), (153, 0, 204), (204, 0, 153), (10, 71, 255), (204, 0, 51), (0, 204, 153), (255, 194, 10), (0, 204, 51), (71, 117, 255), ]

        for district in districts:
            color = colors[district - 1]

            year_counts = [business.models.License.objects.filter(district=district).filter(license_year=str(year)).count() for year in years]

            district_data = {"fill": False, "lineTension": 0.1, "backgroundColor": "rgba({},{},{},0.4)".format(*color), "borderColor": "rgba({},{},{},1)".format(*color), "borderCapStyle": 'butt', "borderDash": [], "borderDashOffset": 0.0, "borderJoinStyle": 'miter', "pointBorderColor": "rgba({},{},{},1)".format(*color), "pointBackgroundColor": "#fff", "pointBorderWidth": 1, "pointHoverRadius": 5, "pointHoverBackgroundColor": "rgba({},{},{},1)".format(*color), "pointHoverBorderColor": "rgba(220,220,220,1)", "pointHoverBorderWidth": 2, "pointRadius": 1, "pointHitRadius": 10, "spanGaps": False,}

            district_data["label"] = "District {}".format(district)
            district_data["data"] = year_counts

            data['datasets'].append(district_data)

        return JsonResponse(data)




class LicensesByBusinessClassView(View):
    template = 'business/licenses_by_business_class.html'

    def __str__(self):
        return 'LicensesByBusinessClassView'

    def get(self, request):
        return render_to_response(self.template)


class LicensesByBusinessClassDataView(View):

    def __str__(self):
        return 'LicensesByBusinessClassDataView'

    def get(self, request):
        years = range(1990, 2017)

        biz_classes = list(business.models.License.objects.filter(business_class__isnull=False).values_list('business_class', flat=True).distinct())

        data = {"labels": list(years), "datasets": []}

        colors = [ (0, 51, 204), (153, 0, 204), (204, 0, 153), (10, 71, 255), (204, 0, 51), (0, 204, 153), (255, 194, 10), (0, 204, 51), (71, 117, 255), (255, 0, 191), (255, 222, 122), (191, 255, 0), (32, 128, 0), (128, 0, 32), ]

        i = 0
        for biz_class in biz_classes:
            color = colors[i]

            year_counts = [business.models.License.objects.filter(business_class=biz_class).filter(license_year=str(year)).count() for year in years]

            biz_class_data = {"fill": False, "lineTension": 0.1, "backgroundColor": "rgba({},{},{},0.4)".format(*color), "borderColor": "rgba({},{},{},1)".format(*color), "borderCapStyle": 'butt', "borderDash": [], "borderDashOffset": 0.0, "borderJoinStyle": 'miter', "pointBorderColor": "rgba({},{},{},1)".format(*color), "pointBackgroundColor": "#fff", "pointBorderWidth": 1, "pointHoverRadius": 5, "pointHoverBackgroundColor": "rgba({},{},{},1)".format(*color), "pointHoverBorderColor": "rgba(220,220,220,1)", "pointHoverBorderWidth": 2, "pointRadius": 1, "pointHitRadius": 10, "spanGaps": False,}

            biz_class_data["label"] = biz_class
            biz_class_data["data"] = year_counts

            data['datasets'].append(biz_class_data)
            i += 1

        return JsonResponse(data)


