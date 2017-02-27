# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0008_auto_20160420_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highscores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('game', models.CharField(max_length=255)),
                ('scores', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='games',
            field=models.ForeignKey(to='gamestore.UserProfile', related_name='games', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='my_highscores',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.OneToOneField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='game',
            field=models.OneToOneField(to='gamestore.Game', related_name='sales', null=True),
        ),
    ]
