from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from experiments import views_calculator
from experiments import views_file
from experiments import views_user_group

router = SimpleRouter()
router.register(r'users', views_user_group.UserViewSet)
router.register(r'groups', views_user_group.GroupViewSet)

# API endpoints for UserViewSet and GroupViewSet
urlpatterns = [
    url(r'^experiments/', include(router.urls)),
]

# More API endpoints
urlpatterns += [
    # Calulator
    url(r'^experiments/calculator/add/(?P<numbers>.*)/$',
        views_calculator.add),

    # File
    url(r'^experiments/file/pdf/$', views_file.pdf),
    url(r'^experiments/file/zip/$', views_file.zip),
    url(r'^experiments/image/jpeg/$', views_file.jpeg),
]
