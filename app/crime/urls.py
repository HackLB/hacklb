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

import crime.views
import crime.viewsets

from rest_framework import routers


urlpatterns = [
    url(r'^$', crime.views.HomeView.as_view(), name='crime_home'),
    url(r'^incident/(?P<guid>.*)$', crime.views.IncidentView.as_view(), name='crime_incident_details'),
]

router = routers.DefaultRouter()
router.register(r'incident', crime.viewsets.IncidentViewSet)
router.register(r'incidentgeo', crime.viewsets.IncidentGeoViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
