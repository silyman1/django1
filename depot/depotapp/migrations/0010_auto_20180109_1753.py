# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0009_auto_20180109_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='buyer_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='seller_del',
            field=models.BooleanField(default=False),
        ),
    ]
