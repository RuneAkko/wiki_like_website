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


class News(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(primary_key=True, max_length=249)
    date = models.CharField(max_length=45, blank=True, null=True)
    text = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class News2(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(primary_key=True, max_length=249)
    datetime = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news2'
