from django.conf.urls import patterns, url
from django.conf import settings
from data import views

urlpatterns = patterns('',
    url(r'^AMA1/', views.AMA1, name = 'AMA1'),
    url(r'^existingAMA1/(?P<data_id>\w+)/$', views.existingAMA1, name='existingAMA1'),
)
