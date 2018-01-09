# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0005_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_time', models.DateTimeField(verbose_name=b'date to order')),
                ('deliver_time', models.DateTimeField(null=True, verbose_name=b'date to deliver')),
                ('received_time', models.DateTimeField(null=True, verbose_name=b'date to receive')),
                ('is_receiver', models.BooleanField(default=False)),
                ('is_deliver', models.BooleanField(default=False)),
                ('buyer', models.CharField(max_length=100)),
                ('seller', models.CharField(max_length=100)),
                ('product', models.OneToOneField(to='depotapp.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
