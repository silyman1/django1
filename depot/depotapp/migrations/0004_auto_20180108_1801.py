# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0003_auto_20180108_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=24, decimal_places=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='lineitem',
            old_name='product',
            new_name='pro_item',
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='cart_name',
            field=models.ManyToManyField(to='depotapp.Cart'),
        ),
    ]
