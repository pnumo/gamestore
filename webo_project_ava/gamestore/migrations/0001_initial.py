# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('price', models.IntegerField()),
                ('soldDate', models.DateTimeField()),
                ('game', models.ForeignKey(to='gamestore.Game')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('money', models.IntegerField()),
                ('is_dev', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.OneToOneField(null=True, to='gamestore.UserProfile'),
        ),
        migrations.AddField(
            model_name='game',
            name='purchaser',
            field=models.ForeignKey(to='gamestore.UserProfile', related_name='purchasers'),
        ),
    ]
