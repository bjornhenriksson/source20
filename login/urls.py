from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^try/', views.trylogin, name='trylogin'),
    url(r'^landing/', views.tracker, name='tracker'),
)