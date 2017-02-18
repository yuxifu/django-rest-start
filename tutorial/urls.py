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
from django.conf import settings

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

import oauth2_provider.views as oauth2_views

# from .swagger import SwaggerSchemaView

swagger_view = get_swagger_view(title='Amazing API')
# custom swagger_view
# swagger_view = SwaggerSchemaView.as_view()

schema_view = get_schema_view(title='Amazing API')

# Routers provide an easy way of automatically determining the URL conf
# router = routers.DefaultRouter()

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]


urlpatterns = [
    #
    # url(r'^', include(router.urls)),

    # admin views
    url(r'^admin/', admin.site.urls),

    # account views
    url(r'^accounts/', include('django.contrib.auth.urls')),

    # http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    # django-oauth-toolkit, oauth2
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^o/', include(oauth2_endpoint_views, namespace="oauth2_provider")),

    # https://django-rest-swagger.readthedocs.io/en/latest/
    url(r'^swagger/$', swagger_view, name='swagger-root'),

    # http://drfdocs.com/
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API schemas
    # http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/
    url(r'^schema/$', schema_view),

    # App 'snippets'
    url(r'^', include('snippets.urls')),

    # App 'experiments'
    url(r'^', include('experiments.urls')),

    # App 'apiAdmin'
    url(r'^', include('apiAdmin.urls')),
]
