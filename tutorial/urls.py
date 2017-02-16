"""tutorial URL Configuration

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
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

swagger_view = get_swagger_view(title='Tutorial API')

schema_view = get_schema_view(title='Tutorial API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # https://django-rest-swagger.readthedocs.io/en/latest/
    url(r'^swagger/$', swagger_view),

    # API schemas
    # http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/
    url(r'^schema/$', schema_view),

    # http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    # http://drfdocs.com/
    url(r'^docs/', include('rest_framework_docs.urls')),

    # App 'snippets'
    url(r'^', include('snippets.urls')),

    # App 'experiments'
    url(r'^', include('experiments.urls')),
]
