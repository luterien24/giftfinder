# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_category_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Hediye', 'verbose_name_plural': 'Hediyeler'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Be\u011feni', 'verbose_name_plural': 'Be\u011feniler'},
        ),
        migrations.AlterModelOptions(
            name='occasion',
            options={'verbose_name': '\xd6zel G\xfcn', 'verbose_name_plural': '\xd6zel G\xfcnler'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'verbose_name': 'Ki\u015fi', 'verbose_name_plural': 'Ki\u015filer'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Ma\u011faza', 'verbose_name_plural': 'Ma\u011fazalar'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Etiket', 'verbose_name_plural': 'Etiketler'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='max_price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='min_price',
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(null=True, verbose_name='Fiyat', max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0130sim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(verbose_name='Kategori', blank=True, to='items.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(verbose_name='Kategori', blank=True, to='items.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=b'story/images/', null=True, verbose_name='Resim', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='max_age',
            field=models.IntegerField(verbose_name='Max. Ya\u015f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='min_age',
            field=models.IntegerField(verbose_name='Min. Ya\u015f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0130sim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='recipients',
            field=models.ManyToManyField(to='items.Recipient', null=True, verbose_name='Hediye Al\u0131nabilecek Ki\u015filer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='sex',
            field=models.CharField(default=b'both', max_length=200, verbose_name='Cinsiyet', choices=[(b'man', b'Man'), (b'woman', b'Woman'), (b'both', b'Both')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='items.Tag', null=True, verbose_name='Etiketler', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='item',
            field=models.ForeignKey(verbose_name='Hediye', blank=True, to='items.Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Like Say\u0131s\u0131'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occasion',
            name='about',
            field=models.TextField(null=True, verbose_name='Hakk\u0131nda', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occasion',
            name='ending_date',
            field=models.DateTimeField(null=True, verbose_name='Biti\u015f Tarihi', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occasion',
            name='gifts',
            field=models.ManyToManyField(to='items.Item', null=True, verbose_name='Hediyeler', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occasion',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0130sim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occasion',
            name='starting_date',
            field=models.DateTimeField(null=True, verbose_name='Ba\u015flang\u0131\xe7 Tarihi', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0130sim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='items',
            field=models.ManyToManyField(to='items.Item', null=True, verbose_name='Hediyeler', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0130sim'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Ki\u015filer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Ba\u015fl\u0131k'),
            preserve_default=True,
        ),
    ]
