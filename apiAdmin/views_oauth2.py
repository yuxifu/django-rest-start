"""
Sysadmin views - oauth2
"""

import json

from braces.views import CsrfExemptMixin
from oauth2_provider.oauth2_backends import OAuthLibCore
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics

from .serializers import OAuth2PasswordAccessTokenRequestFieldsSerializer


class tokenView(CsrfExemptMixin, OAuthLibMixin, generics.GenericAPIView):
    """
    Provide access token for grant type 'password'.
    """
    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = OAuthLibCore
    permission_classes = (permissions.AllowAny,)
    serializer_class = OAuth2PasswordAccessTokenRequestFieldsSerializer

    def post(self, request, *args, **kwargs):
        # Use the rest framework `.data` to fake the post body of the django
        # request.

        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status = self.create_token_response(
            request._request)
        response = Response(data=json.loads(body), status=status)

        for k, v in headers.items():
            response[k] = v
        return response
