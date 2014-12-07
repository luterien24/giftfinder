from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from apps.profiles.models import Profile

SEX_CHOICES = (
	('man', 'Man'),
	('woman', 'Woman'),
	('both', 'Both')
)

class Item(models.Model):
	""" hediye """
	name = models.CharField(_("Name"), max_length=200)
	image = models.ImageField(_("Image"), upload_to="story/images/", null=True, blank=True)
	max_price = models.DecimalField(_("Maximum Price"), max_digits=8, decimal_places=2)
	min_price = models.DecimalField(_("Minimum Price"), max_digits=8, decimal_places=2)
	max_age = models.IntegerField(_("Maximum Age"))
	min_age = models.IntegerField(_("Minimum Age"))
	tags = models.ManyToManyField("Tag", verbose_name=_("Tags"), null=True, blank=True)
	sex = models.CharField(_("Sex"), max_length=200, choices=SEX_CHOICES, default="man")
	category = models.ForeignKey("Category", verbose_name=_("Category"), null=True, blank=True)
	recipients = models.ManyToManyField("Recipient", verbose_name=_("Recipients"), null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name)

	class Meta:
		verbose_name = _("Gift")


class Tag(models.Model):
	"""
		mobil'de ilgi alani olarak gececek

		ornek, bilgisayar icin;

		oyun, internet

	"""
	name = models.CharField(_("Name"), max_length=200)

	def __unicode__(self):
		return "%s" % (self.name)


class Category(models.Model):
	""" ev esyasi, el yapimi, cocuklar icin, teknoloji, nostalji vs """
	name = models.CharField(_("Name"), max_length=200)

	def __unicode__(self):
		return "%s" % (self.name)


class Recipient(models.Model):
	""" aile, akraba, arkadas, sevgili, es, tanidik vs """
	name = models.CharField(_("Name"), max_length=200)

	def __unicode__(self):
		return "%s" % (self.name)


class Occasion(models.Model):
	"""
		ozel gunler
		bu gunlere bagli panelden heiye secimi yapilacak
	"""
	name = models.CharField(_("Name"), max_length=200)
	starting_date = models.DateTimeField(_("Name"), null=True, blank=True)
	ending_date = models.DateTimeField(_("Name"), null=True, blank=True)
	about = models.TextField(_("About"), null=True, blank=True)
	gifts = models.ManyToManyField(Item, verbose_name=_("Recipients"), null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name)


class Store(models.Model):
	""" magaza """
	name = models.CharField(_("Name"), max_length=200)
	owners = models.ManyToManyField(Profile, verbose_name=_("Profiles"), null=True, blank=True)
	items = models.ManyToManyField(Item, verbose_name=_("Items"), null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name)



class Like(models.Model):
	item = models.ForeignKey(Item, verbose_name=_("Item"), null=True, blank=True)
	likes = models.IntegerField(_("Maximum Age"), default=0)

	def __unicode__(self):
		return "%s received %s likes" % (self.item, self.likes)

