# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('publish', models.BooleanField(default=False)),
                ('created', models.DateTimeField(verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'ordering': ['-created'],
                'verbose_name_plural': 'Blog Posts',
            },
            bases=(models.Model,),
        ),
    ]
