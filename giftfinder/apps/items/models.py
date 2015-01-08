# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from apps.profiles.models import Profile

SEX_CHOICES = (
	('man', u'Erkek'),
	('woman', u'Bayan'),
	('both', u'Hepsi')
)

class Item(models.Model):
	""" hediye """
	name = models.CharField(_(u"İsim"), max_length=200)
	image = models.ImageField(_(u"Resim"), upload_to="story/images/", null=True, blank=True)
	price = models.DecimalField(_(u"Fiyat"), max_digits=8, decimal_places=2, null=True, blank=True)
	description = models.TextField(_(u"Açıklama"), null=True, blank=True)
	max_age = models.IntegerField(_(u"Max. Yaş"))
	min_age = models.IntegerField(_(u"Min. Yaş"))
	tags = models.ManyToManyField('Tag', verbose_name=_(u"Etiketler"), null=True, blank=True)
	sex = models.CharField(_(u"Cinsiyet"), max_length=200, choices=SEX_CHOICES, default="both")
	category = models.ForeignKey("Category", verbose_name=_(u"Kategori"), null=True, blank=True)
	recipients = models.ManyToManyField("Recipient", verbose_name=_(u"Hediye Alınabilecek Kişiler"), null=True, blank=True)

	# temporary fields
	store_url = models.TextField(_(u"Satın Alınabilecek URL"), null=True, blank=True)
	store_name = models.CharField(_(u"Satın Alınabilecek Sitenin İsmi"), max_length=80, null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name)

	class Meta:
		verbose_name = _(u"Hediye")
		verbose_name_plural = _(u"Hediyeler")


class Tag(models.Model):
	"""
		mobil'de ilgi alani olarak gececek

		ornek, bilgisayar icin;

		oyun, internet

	"""
	name = models.CharField(_(u"Başlık"), max_length=200)

	class Meta:
		verbose_name = _(u"Etiket")
		verbose_name_plural = _(u"Etiketler")

	def __unicode__(self):
		return "%s" % (self.name)


class Category(models.Model):
	""" ev esyasi, el yapimi, cocuklar icin, teknoloji, nostalji vs """
	parent = models.ForeignKey('Category', verbose_name=_(u'Kategori'), null=True, blank=True)
	name = models.CharField(_(u"İsim"), max_length=200)

	class Meta:
		verbose_name = _(u"Kategori")
		verbose_name_plural = _(u"Kategoriler")

	def __unicode__(self):
		return "%s" % (self.name)


class Recipient(models.Model):
	""" aile, akraba, arkadas, sevgili, es, tanidik vs """
	name = models.CharField(_(u"İsim"), max_length=200)

	class Meta:
		verbose_name = _(u"Kişi")
		verbose_name_plural = _(u"Kişiler")

	def __unicode__(self):
		return "%s" % (self.name)


class Occasion(models.Model):
	"""
		ozel gunler
		bu gunlere bagli panelden heiye secimi yapilacak
	"""
	name = models.CharField(_(u"İsim"), max_length=200)
	starting_date = models.DateTimeField(_(u"Başlangıç Tarihi"), null=True, blank=True)
	ending_date = models.DateTimeField(_(u"Bitiş Tarihi"), null=True, blank=True)
	about = models.TextField(_(u"Hakkında"), null=True, blank=True)
	gifts = models.ManyToManyField(Item, verbose_name=_(u"Hediyeler"), null=True, blank=True)

	class Meta:
		verbose_name = _(u"Özel Gün")
		verbose_name_plural = _(u"Özel Günler")

	def __unicode__(self):
		return "%s" % (self.name)


class Store(models.Model):
	""" magaza """
	name = models.CharField(_(u"İsim"), max_length=200)
	owners = models.ManyToManyField(Profile, verbose_name=_(u"Kişiler"), null=True, blank=True)
	items = models.ManyToManyField(Item, verbose_name=_(u"Hediyeler"), null=True, blank=True)

	class Meta:
		verbose_name = _(u"Mağaza")
		verbose_name_plural = _(u"Mağazalar")

	def __unicode__(self):
		return "%s" % (self.name)



class Like(models.Model):
	item = models.ForeignKey(Item, verbose_name=_(u"Hediye"), null=True, blank=True)
	likes = models.IntegerField(_(u"Like Sayısı"), default=0)

	class Meta:
		verbose_name = _(u"Beğeni")
		verbose_name_plural = _(u"Beğeniler")

	def __unicode__(self):
		return "%s received %s likes" % (self.item, self.likes)

