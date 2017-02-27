# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0011_auto_20160424_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='my_highscores',
        ),
    ]
