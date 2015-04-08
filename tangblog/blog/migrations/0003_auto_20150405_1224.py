# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150405_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.AddField(
            model_name='post',
            name='publish_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
