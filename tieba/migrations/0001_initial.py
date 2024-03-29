# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-15 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommentCopy',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comment_copy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommentCopy1',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comment_copy1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.CharField(blank=True, max_length=30, null=True)),
                ('comment_num', models.IntegerField(blank=True, null=True)),
                ('thread_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostCopy',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('comment_num', models.IntegerField(blank=True, null=True)),
                ('thread_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'post_copy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostCopy1',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.CharField(blank=True, max_length=30, null=True)),
                ('comment_num', models.IntegerField(blank=True, null=True)),
                ('thread_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'post_copy1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('reply_num', models.IntegerField(blank=True, null=True)),
                ('good', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'thread',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadCopy',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('reply_num', models.IntegerField(blank=True, null=True)),
                ('good', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'thread_copy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadCopy1',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('reply_num', models.IntegerField(blank=True, null=True)),
                ('good', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'thread_copy1',
                'managed': False,
            },
        ),
    ]
