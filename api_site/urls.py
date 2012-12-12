from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tasty/', include('tasty.urls')),
    url(r'^rest/', include('rest.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
