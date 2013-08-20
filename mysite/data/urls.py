from django.conf.urls import patterns, url
from django.conf import settings
from data import views

urlpatterns = patterns('',
#    url(r'^$', views.new, name='index'),
    url(r'^getcsv/(?P<project_name>\w+)/$', views.getCSV, name='getCSV'),
    url(r'^$', views.show, name='index'),
    url(r'^snapshot/(?P<data_id>\w+)/$', views.snapshot_detail, name='detail'),
    url(r'^timemachine/(?P<data_id>\w+)/$', views.timemachine, name='timemachine'),
    url(r'^(?P<data_id>\w+)/$', views.detail, name='detail'),
#    url(r'^(?P<data_id>\w+)/(?P<project_name>\w+)/$', views.detail, name='detail'),
    url(r'^create/', views.create, name = 'create'),
    url(r'^new/', views.new, name = 'new'),
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root', settings.STATIC_ROOT} ),
)
