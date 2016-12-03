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
from django.views.static import serve as static_serve


# Enable Django Admin site
urlpatterns = [
    url(r'^admin/', admin.site.urls)
]

# Enable MEDIA and STATIC serving
urlpatterns += [
    url(r'^media/(?P<path>.*)$', static_serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', static_serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]


# Enable URL files from custom Django apps
urlpatterns += [
    url(r'^', include('core.urls')),
    url(r'^crime/', include('crime.urls')),
    url(r'^legistar/', include('legistar.urls')),
    url(r'^geographic/', include('geographic.urls')),
]


# Enable debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
