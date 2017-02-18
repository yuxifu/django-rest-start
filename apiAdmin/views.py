"""
Sysadmin views
"""
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    """API Root"""
    return Response({
        'swagger': reverse('swagger-root', request=request, format=format),
        'users': reverse('snippets-user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
