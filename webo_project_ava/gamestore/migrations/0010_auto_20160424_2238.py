# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0009_auto_20160424_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='my_highscores',
            field=models.TextField(null=True),
        ),
    ]
