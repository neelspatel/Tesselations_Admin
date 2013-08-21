from django.conf.urls import patterns, url
from django.conf import settings
from data import views

urlpatterns = patterns('',
    url(r'^AMA1/$', views.main, name = 'AMA1'),
    url(r'^AMA1/download/$', views.csv, name = 'AMA1'),
    url(r'^AMA1/save/$', views.saveAMA1, name = 'AMA1'),
    url(r'^AMA1/new/$', views.newAMA1, name = 'AMA1'),
    url(r'^AMA1/list/$', views.list, name = 'list'),
    url(r'^AMA1/(?P<data_id>\w+)/$', views.existingAMA1, name='existingAMA1'),
)
