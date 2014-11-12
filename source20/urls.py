from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^get_class/', include('get_class.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
