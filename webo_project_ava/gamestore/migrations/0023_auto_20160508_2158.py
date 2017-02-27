# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0022_auto_20160507_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='game',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 5, 8)),
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
