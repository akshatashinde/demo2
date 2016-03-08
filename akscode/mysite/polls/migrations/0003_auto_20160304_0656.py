# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=2, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(default='L', max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='polls.Musician'),
        ),
    ]
