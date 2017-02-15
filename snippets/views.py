"""
method 4: Class based views (generic views).
rest_framework_swagger: Get/Delete OK; POST/PUT OK
controls
"""
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    """
    Snippet List
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Snippet Detail"""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    """User List"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """User Detail"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """API Root"""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    """Snippet Highlight"""
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
