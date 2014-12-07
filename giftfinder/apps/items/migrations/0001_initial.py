# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('image', models.ImageField(upload_to=b'story/images/', null=True, verbose_name='Image', blank=True)),
                ('max_price', models.DecimalField(verbose_name='Maximum Price', max_digits=8, decimal_places=2)),
                ('min_price', models.DecimalField(verbose_name='Minimum Price', max_digits=8, decimal_places=2)),
                ('max_age', models.IntegerField(verbose_name='Maximum Age')),
                ('min_age', models.IntegerField(verbose_name='Minimum Age')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='items.Category', null=True)),
            ],
            options={
                'verbose_name': 'Gift',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('starting_date', models.DateTimeField(null=True, verbose_name='Name', blank=True)),
                ('ending_date', models.DateTimeField(null=True, verbose_name='Name', blank=True)),
                ('about', models.TextField(null=True, verbose_name='About', blank=True)),
                ('gifts', models.ManyToManyField(to='items.Item', null=True, verbose_name='Recipients', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('items', models.ManyToManyField(to='items.Item', null=True, verbose_name='Items', blank=True)),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Profiles', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='recipients',
            field=models.ManyToManyField(to='items.Recipient', null=True, verbose_name='Recipients', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='items.Tag', null=True, verbose_name='Tags', blank=True),
            preserve_default=True,
        ),
    ]
