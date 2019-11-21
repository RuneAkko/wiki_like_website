# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class CommentCopy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_copy'


class CommentCopy1(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_copy1'


class Post(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    floor = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    thread_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostCopy(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    floor = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    thread_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_copy'


class PostCopy1(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    floor = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    thread_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_copy1'


class Thread(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    reply_num = models.IntegerField(blank=True, null=True)
    good = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thread'


class ThreadCopy(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    reply_num = models.IntegerField(blank=True, null=True)
    good = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thread_copy'


class ThreadCopy1(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    reply_num = models.IntegerField(blank=True, null=True)
    good = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thread_copy1'
