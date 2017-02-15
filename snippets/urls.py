from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views0
from snippets import views1
from snippets import views2
from snippets import views3
from snippets import views4
from snippets import views

# different ways to create API
urlpatterns = [
    url(r'^snippets0/$', views0.snippet_list),
    url(r'^snippets0/(?P<pk>[0-9]+)/$', views0.snippet_detail),
    url(r'^snippets1/$', views1.snippet_list),
    url(r'^snippets1/(?P<pk>[0-9]+)$', views1.snippet_detail),
    url(r'^snippets2/$', views2.SnippetList.as_view()),
    url(r'^snippets2/(?P<pk>[0-9]+)/$', views2.SnippetDetail.as_view()),
    url(r'^snippets3/$', views3.SnippetList.as_view()),
    url(r'^snippets3/(?P<pk>[0-9]+)/$', views3.SnippetDetail.as_view()),
    url(r'^snippets4/$', views4.SnippetList.as_view()),
    url(r'^snippets4/(?P<pk>[0-9]+)/$', views4.SnippetDetail.as_view()),
]

# API endpoints
urlpatterns += format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])

