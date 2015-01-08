# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20150108_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(null=True, verbose_name='A\xe7\u0131klama', blank=True),
            preserve_default=True,
        ),
    ]
