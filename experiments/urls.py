from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from experiments import views_calculator
from experiments import views_file

# More API endpoints
urlpatterns = [
    # Calulator
    url(r'^experiments/calculator/add/(?P<numbers>.*)/$',
        views_calculator.add),

    # File
    url(r'^experiments/file/pdf/$', views_file.pdf),
    url(r'^experiments/file/zip/$', views_file.zip),
    url(r'^experiments/image/jpeg/$', views_file.jpeg),
]
