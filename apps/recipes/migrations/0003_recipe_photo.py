# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150123_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
    ]
