from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = {
    url(r'^$', views.tieba),
    url(r'tieba_content_(\d+)/', views.tieba_content),
    url(r'tieba_content2_(\d+)/', views.tieba_content2),
    url(r'tieba_content3_(\d+)/', views.tieba_content3),
    url(r'picture_show_tieba/', views.show)
    # url(r'tieba_contentend')
    # url(r'thread_(.+)$'),
    # url(r'map_topic_(\d+)$', views.map_topic),
    # url(r'map_topic_(\d+)/(.+)/(\d+)$', views.map_middle),
}
