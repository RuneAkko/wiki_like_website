from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = {
    url(r'^$', views.map),
    url(r'map_topic_(\d+)$', views.map_topic),
    url(r'map_topic_(\d+)/(.+)/(\d+)$', views.map_middle),
}