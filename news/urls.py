from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = {
    url(r'^$', views.news),
    url(r'news_content_(\d+)/', views.news_content),
    url(r'news_picture_show/', views.picture_show)
    # url(r'news_content/(.+)$', views.news_contentend)
}