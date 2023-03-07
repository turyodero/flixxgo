from django import template
from django.template.library import register_filter

register = template.Library()

@register.filter(name='type')
def type_filter(value):
    return type(value).__name__
