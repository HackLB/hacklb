"""HackLB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

import business.views
import business.viewsets

from rest_framework import routers

urlpatterns = [
    url(r'^$', business.views.HomeView.as_view(), name='business_home'),
    url(r'^licenses_by_district/$', business.views.LicensesByDistrictView.as_view(), name='business_licenses_by_district'),
    url(r'^licenses_by_district/data.json', business.views.LicensesByDistrictDataView.as_view(), name='business_licenses_by_district_data'),
    
    url(r'^licenses_by_business_class/$', business.views.LicensesByBusinessClassView.as_view(), name='business_licenses_by_business_class'),
    url(r'^licenses_by_business_class/data.json', business.views.LicensesByBusinessClassDataView.as_view(), name='business_licenses_by_business_class_data'),
]

router = routers.DefaultRouter()
router.register(r'dataset', business.viewsets.DatasetViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
