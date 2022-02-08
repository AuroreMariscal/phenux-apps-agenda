#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "events"
urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='list'),
    url(r'^event/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]