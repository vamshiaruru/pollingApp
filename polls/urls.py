from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lastViewed/$', views.last_viewed, name='last_viewed'),
    url(r'^(?P<question>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question>[0-9]+)/vote/$', views.vote, name='vote'),

]