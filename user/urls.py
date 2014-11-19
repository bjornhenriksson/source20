from django.conf.urls import patterns, url

from user import views

urlpatterns = patterns('',
    url(r'^$', views.redirect, name='redirect'),
    url(r'^login/', views.trylogin, name='trylogin'),
    url(r'^landing/', views.tracker, name='tracker'),
)