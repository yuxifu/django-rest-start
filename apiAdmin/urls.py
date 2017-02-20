from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.views.generic import RedirectView

from apiAdmin import views, views_oauth2

# API endpoints for UserViewSet and GroupViewSet
router = SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# API endpoints
urlpatterns = [
    # url(r'^$', views.api_root),

    # API endpoints for UserViewSet and GroupViewSet
    url(r'^administration/', include(router.urls)),

    # Token
    url(r'^administration/token/?$', views_oauth2.tokenView.as_view(), name="access-token"),

    # sign up end point
    url(r'^administration/signup/$', views.SignUp.as_view(), name="sign-up"),

    # redirect root to swagger UI
    url(r'^$', RedirectView.as_view(url='/swagger/')),
]

