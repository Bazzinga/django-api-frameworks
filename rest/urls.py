# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = patterns('rest.views',
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^logs/$', LogEntryList.as_view(), name='logentry-list'),
    url(r'^logs/(?P<pk>\d+)/$', LogEntryDetail.as_view(), name='logentry-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

