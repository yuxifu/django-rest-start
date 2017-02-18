from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.views.generic import RedirectView

from apiAdmin import views


# API endpoints
urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^$', RedirectView.as_view(url='/swagger/')),
]
