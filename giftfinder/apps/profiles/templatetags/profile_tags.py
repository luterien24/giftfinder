from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.assignment_tag
def test(user):
	pass
