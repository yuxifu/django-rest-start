from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from experiments import views_calculator
from experiments import views_file

# API endpoints
urlpatterns = format_suffix_patterns([
    # Calulator
    url(r'^experiments/calculator/add/(?P<numbers>.*)/$',
        views_calculator.add),

    # File
    url(r'^experiments/file/pdf/$', views_file.pdf),
    url(r'^experiments/file/zip/$', views_file.zip),
    url(r'^experiments/image/jpeg/$', views_file.jpeg),
])
