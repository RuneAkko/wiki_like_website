# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BlogDetail(models.Model):
    url = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    push_date = models.CharField(max_length=45, blank=True, null=True)
    viewtime = models.CharField(max_length=45, blank=True, null=True)
    blog_content = models.CharField(max_length=20000, blank=True, null=True)
    comment_num = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_detail'
