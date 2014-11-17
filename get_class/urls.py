from django.conf.urls import patterns, url

from get_class import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^voteup/', views.vote_up, name='vote_up'),
    url(r'^votedown/', views.vote_down, name='vote_down'),
    url(r'^logout/', views.log_out, name='log_out'),
)