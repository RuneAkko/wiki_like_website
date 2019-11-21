# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Post(models.Model):
    post_url = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    pt_time = models.CharField(max_length=100, blank=True, null=True)
    good_num = models.IntegerField(blank=True, null=True)
    comm_num = models.IntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    repost_num = models.IntegerField(primary_key=True,blank=True, null=False)
    poster_url = models.CharField(max_length=255, blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=False, primary_key=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class User(models.Model):
    userid = models.CharField(max_length=255, blank=True, null=False, primary_key=True)
    tweets_num = models.IntegerField(blank=True, null=False, primary_key=True)
    follow_num = models.IntegerField(blank=True, null=True)
    fan_num = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    authentication = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
