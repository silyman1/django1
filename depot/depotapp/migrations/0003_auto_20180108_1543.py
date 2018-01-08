# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0002_auto_20180108_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineitem',
            old_name='time_to_market',
            new_name='time_to_cart',
        ),
    ]
