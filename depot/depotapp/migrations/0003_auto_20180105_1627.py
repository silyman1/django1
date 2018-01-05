# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0002_auto_20180105_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='store_product_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
