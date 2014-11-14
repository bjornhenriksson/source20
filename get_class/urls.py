from django.conf.urls import patterns, url

from get_class import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^voteup/', views.vote_up, name='vote_up'),
)