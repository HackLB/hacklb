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

import legistar.views
import legistar.viewsets

from rest_framework import routers


urlpatterns = [
    url(r'^$', legistar.views.HomeView.as_view(), name='legistar_home'),
    url(r'^body/(?P<guid>.*)$', legistar.views.BodyView.as_view(), name='body_details'),
    url(r'^document/(?P<guid>.*)$', legistar.views.DocumentView.as_view(), name='document_details'),
    url(r'^meeting/(?P<guid>.*)$', legistar.views.MeetingView.as_view(), name='meeting_details'),
    url(r'^agendaitem/(?P<guid>.*)$', legistar.views.AgendaItemView.as_view(), name='agendaitem_details'),
]

router = routers.DefaultRouter()
router.register(r'body', legistar.viewsets.BodyViewSet)
router.register(r'document', legistar.viewsets.DocumentViewSet)
router.register(r'meeting', legistar.viewsets.MeetingViewSet)
router.register(r'agendaitem', legistar.viewsets.AgendaItemViewSet)

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
