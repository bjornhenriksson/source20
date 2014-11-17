from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^', views.trylogin, name='trylogin'),
)