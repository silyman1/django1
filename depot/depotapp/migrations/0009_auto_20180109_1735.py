# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0008_auto_20180109_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='user',
        ),
        migrations.AddField(
            model_name='myorder',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
