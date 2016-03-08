# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_example_fruit_ox'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Example',
        ),
        migrations.DeleteModel(
            name='Ox',
        ),
    ]
