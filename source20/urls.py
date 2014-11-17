from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^get_class/', include('get_class.urls', namespace="get_class")),
    url(r'^login/', include('login.urls', namespace="log_in")),
    url(r'^admin/', include(admin.site.urls)),
)
