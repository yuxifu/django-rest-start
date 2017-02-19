"""
Sysadmin views
"""
from django.contrib.auth.models import User, Group

from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from security.permissions import IsAuthenticatedOrCreate

from apiAdmin.serializers import SignUpSerializer, UserSerializer, GroupSerializer


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    """API Root"""
    return Response({
        'swagger': reverse('swagger-root', request=request, format=format),
        'users': reverse('snippets-user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SignUp(generics.CreateAPIView):
    """
    Sign up or register as a new user
    """
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class UserViewSet(viewsets.ModelViewSet):
    """
    List or modify users
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    List or modify groups
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
