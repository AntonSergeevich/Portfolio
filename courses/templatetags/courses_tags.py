from django import template
from courses.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_show_category(cat_id=0):
    return Course.objects.filter(cat_id=cat_id)
