# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamestore', '0013_remove_game_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, editable=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='my_highscores',
            field=models.TextField(null=True),
        ),
    ]
