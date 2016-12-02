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
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve as static_serve
from django.contrib import admin
from django.contrib.auth import views as auth_views

import core.views
import core.viewsets

from rest_framework import routers

from haystack.forms import FacetedSearchForm
from haystack.views import FacetedSearchView


urlpatterns = [
    url(r'^$', core.views.HomeView.as_view(), name='home'),
    url(r'^search/$', core.views.CustomFacetedSearchView.as_view(), name='haystack_search'),
]
