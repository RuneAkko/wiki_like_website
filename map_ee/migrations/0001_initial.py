# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-14 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssembleImage',
            fields=[
                ('imageid', models.AutoField(db_column='imageID', primary_key=True, serialize=False)),
                ('imagecontent', models.TextField(blank=True, db_column='imageContent', null=True)),
                ('imageurl', models.CharField(blank=True, db_column='imageUrl', max_length=255, null=True)),
                ('imagewidth', models.FloatField(blank=True, db_column='imageWidth', null=True)),
                ('imageheight', models.FloatField(blank=True, db_column='imageHeight', null=True)),
                ('imagescratchtime', models.DateTimeField(blank=True, db_column='imageScratchTime', null=True)),
                ('imageapi', models.CharField(blank=True, db_column='imageAPI', max_length=255, null=True)),
                ('facetid', models.IntegerField(blank=True, db_column='facetID', null=True)),
                ('topicid', models.IntegerField(blank=True, db_column='topicID', null=True)),
            ],
            options={
                'db_table': 'assemble_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AssembleText',
            fields=[
                ('textid', models.AutoField(db_column='textID', primary_key=True, serialize=False)),
                ('textcontent', models.CharField(blank=True, db_column='textContent', max_length=255, null=True)),
                ('texturl', models.CharField(blank=True, db_column='textUrl', max_length=255, null=True)),
                ('textposttime', models.DateTimeField(blank=True, db_column='textPostTime', null=True)),
                ('textscratchtime', models.DateTimeField(blank=True, db_column='textScratchTime', null=True)),
                ('facetid', models.IntegerField(blank=True, db_column='facetID', null=True)),
                ('topicid', models.IntegerField(blank=True, db_column='topicID', null=True)),
            ],
            options={
                'db_table': 'assemble_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('classid', models.IntegerField(db_column='classID', primary_key=True, serialize=False)),
                ('classname', models.CharField(blank=True, max_length=255, null=True)),
                ('url0', models.CharField(blank=True, max_length=255, null=True)),
                ('sourceid', models.IntegerField(blank=True, db_column='sourceID', null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'domain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facet',
            fields=[
                ('facetid', models.IntegerField(db_column='facetID', primary_key=True, serialize=False)),
                ('facetname', models.CharField(blank=True, db_column='facetName', max_length=255, null=True)),
                ('facetlayer', models.CharField(blank=True, db_column='facetLayer', max_length=255, null=True)),
                ('topicid', models.IntegerField(blank=True, db_column='topicID', null=True)),
                ('facetimage', models.CharField(blank=True, db_column='facetImage', max_length=255, null=True)),
            ],
            options={
                'db_table': 'facet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topicid', models.IntegerField(db_column='topicID', primary_key=True, serialize=False)),
                ('topicname', models.CharField(blank=True, db_column='topicName', max_length=255, null=True)),
                ('topicurl', models.CharField(blank=True, db_column='topicUrl', max_length=255, null=True)),
                ('topiclayer', models.IntegerField(blank=True, db_column='topicLayer', null=True)),
                ('classid', models.IntegerField(blank=True, db_column='classID', null=True)),
                ('fathertopic', models.CharField(blank=True, max_length=255, null=True)),
                ('ftopic_id', models.IntegerField(blank=True, null=True)),
                ('topictype', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TopicRelation',
            fields=[
                ('relationid', models.AutoField(db_column='relationID', primary_key=True, serialize=False)),
                ('parenttopicid', models.IntegerField(blank=True, db_column='parentTopicID', null=True)),
                ('parenttopicname', models.CharField(blank=True, db_column='parentTopicName', max_length=255, null=True)),
                ('parenttopiclayer', models.IntegerField(blank=True, db_column='parentTopicLayer', null=True)),
                ('childtopicid', models.IntegerField(blank=True, db_column='childTopicID', null=True)),
                ('childtopicname', models.CharField(blank=True, db_column='childTopicName', max_length=255, null=True)),
                ('childtopiclayer', models.IntegerField(blank=True, db_column='childTopicLayer', null=True)),
                ('classid', models.IntegerField(blank=True, db_column='classID', null=True)),
            ],
            options={
                'db_table': 'topic_relation',
                'managed': False,
            },
        ),
    ]
