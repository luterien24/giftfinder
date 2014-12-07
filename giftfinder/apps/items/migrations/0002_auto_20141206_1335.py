# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likes', models.IntegerField(default=0, verbose_name='Maximum Age')),
                ('item', models.ForeignKey(verbose_name='Item', blank=True, to='items.Item', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='sex',
            field=models.CharField(default=b'man', max_length=200, verbose_name='Sex', choices=[(b'man', b'Man'), (b'woman', b'Woman'), (b'both', b'Both')]),
            preserve_default=True,
        ),
    ]
