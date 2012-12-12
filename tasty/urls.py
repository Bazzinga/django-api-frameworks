# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url, patterns, include
from tastypie.api import Api

from .resources import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(LogUserResource())
v1_api.register(UserLogsResource())
v1_api.register(UserGroupResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)
