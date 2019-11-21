from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = {

    url('^$', views.weibo),

    url('^weibo_content_(\d+)/', views.weibo_content),

    # url('^weibo_content/$', views.weibo_content),

    url('^weibo_content/(.+)$', views.weibo_contentend),

    url('^picture_show_weibo/', views.show)
}