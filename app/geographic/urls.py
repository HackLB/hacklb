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

import geographic.views
import geographic.viewsets

from rest_framework import routers


urlpatterns = [
    url(r'^$', geographic.views.HomeView.as_view(), name='gis_home'),
    url(r'^dataset/(?P<guid>.*)$', geographic.views.DatasetView.as_view(), name='gis_dataset_details'),
]

router = routers.DefaultRouter()
router.register(r'dataset', geographic.viewsets.DatasetViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
