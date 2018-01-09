# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0007_auto_20180109_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='product',
            field=models.ForeignKey(to='depotapp.Product'),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
