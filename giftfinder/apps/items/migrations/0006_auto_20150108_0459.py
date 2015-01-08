# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='store_name',
            field=models.CharField(max_length=80, null=True, verbose_name='Sat\u0131n Al\u0131nabilecek Sitenin \u0130smi', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='store_url',
            field=models.TextField(null=True, verbose_name='Sat\u0131n Al\u0131nabilecek URL', blank=True),
            preserve_default=True,
        ),
    ]
