# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0012_remove_userprofile_my_highscores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='owner',
        ),
    ]
