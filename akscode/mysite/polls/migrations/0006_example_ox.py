# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160304_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foo_bar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horn_length', models.IntegerField()),
            ],
            options={
                'ordering': ['horn_length'],
                'verbose_name_plural': 'oxen',
            },
        ),
    ]
