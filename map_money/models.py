# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AssembleText(models.Model):
    textid = models.AutoField(db_column='textID', primary_key=True)  # Field name made lowercase.
    textcontent = models.CharField(db_column='textContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    texturl = models.CharField(db_column='textUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    textposttime = models.DateTimeField(db_column='textPostTime', blank=True, null=True)  # Field name made lowercase.
    textscratchtime = models.DateTimeField(db_column='textScratchTime', blank=True, null=True)  # Field name made lowercase.
    facetid = models.IntegerField(db_column='facetID', blank=True, null=True)  # Field name made lowercase.
    topicid = models.IntegerField(db_column='topicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assemble_text'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Domain(models.Model):
    classid = models.IntegerField(db_column='classID', primary_key=True)  # Field name made lowercase.
    classname = models.CharField(max_length=255, blank=True, null=True)
    url0 = models.CharField(max_length=255, blank=True, null=True)
    sourceid = models.IntegerField(db_column='sourceID', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domain'


class Facet(models.Model):
    facetid = models.IntegerField(db_column='facetID', primary_key=True)  # Field name made lowercase.
    facetname = models.CharField(db_column='facetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facetlayer = models.CharField(db_column='facetLayer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    topicid = models.IntegerField(db_column='topicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facet'


class FacetRelation(models.Model):
    relationid = models.AutoField(db_column='relationID', primary_key=True)  # Field name made lowercase.
    parentfacetid = models.IntegerField(db_column='parentFacetID', blank=True, null=True)  # Field name made lowercase.
    parentfacetname = models.CharField(db_column='parentFacetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentfacetlayer = models.IntegerField(db_column='parentFacetLayer', blank=True, null=True)  # Field name made lowercase.
    childfacetid = models.IntegerField(db_column='childFacetID', blank=True, null=True)  # Field name made lowercase.
    childfacetname = models.CharField(db_column='childFacetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childfacetlayer = models.IntegerField(db_column='childFacetLayer', blank=True, null=True)  # Field name made lowercase.
    topicid = models.IntegerField(db_column='topicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facet_relation'


class Topic(models.Model):
    topicid = models.IntegerField(db_column='topicID',primary_key=True)  # Field name made lowercase.
    topicname = models.CharField(db_column='topicName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    topicurl = models.CharField(db_column='topicUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    topiclayer = models.IntegerField(db_column='topicLayer', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', blank=True, null=True)  # Field name made lowercase.
    fathertopic = models.CharField(max_length=255, blank=True, null=True)
    ftopic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic'


class TopicRelation(models.Model):
    relationid = models.AutoField(db_column='relationID', primary_key=True)  # Field name made lowercase.
    parenttopicid = models.IntegerField(db_column='parentTopicID', blank=True, null=True)  # Field name made lowercase.
    parenttopicname = models.CharField(db_column='parentTopicName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parenttopiclayer = models.IntegerField(db_column='parentTopicLayer', blank=True, null=True)  # Field name made lowercase.
    childtopicid = models.IntegerField(db_column='childTopicID', blank=True, null=True)  # Field name made lowercase.
    childtopicname = models.CharField(db_column='childTopicName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childtopiclayer = models.IntegerField(db_column='childTopicLayer', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic_relation'
