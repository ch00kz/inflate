# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USDExchangeRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('average', models.DecimalField(max_digits=10, decimal_places=2)),
                ('high', models.DecimalField(max_digits=10, decimal_places=2)),
                ('low', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
