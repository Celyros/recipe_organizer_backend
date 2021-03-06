# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('reviews', models.TextField(help_text=b'User review here.')),
                ('star', models.PositiveIntegerField(null=True, blank=True)),
                ('username', models.CharField(max_length=20)),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
