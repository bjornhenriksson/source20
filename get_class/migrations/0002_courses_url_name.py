# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='url_name',
            field=models.CharField(default='Unnamed Url', max_length=200),
            preserve_default=True,
        ),
    ]
