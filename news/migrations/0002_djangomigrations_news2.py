# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-16 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News2',
            fields=[
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=249, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'news2',
                'managed': False,
            },
        ),
    ]