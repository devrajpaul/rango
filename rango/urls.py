'''
Created on Jun 16, 2015

@author: edevrpa
'''
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))