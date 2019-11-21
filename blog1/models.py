# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Articles(models.Model):
    title = models.CharField(primary_key=True, max_length=100)
    create_date = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    url_object_id = models.CharField(max_length=45, blank=True, null=True)
    front_image_url = models.CharField(max_length=100, blank=True, null=True)
    front_image_path = models.CharField(max_length=100, blank=True, null=True)
    praise_nums = models.CharField(max_length=45, blank=True, null=True)
    fav_nums = models.CharField(max_length=45, blank=True, null=True)
    content = models.CharField(max_length=20000, blank=True, null=True)
    tags = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'
