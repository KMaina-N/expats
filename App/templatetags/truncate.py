from django import template
from django.utils.text import Truncator

register = template.Library()

@register.filter
def truncate_text(value, length):
    return value[:length] + "..." if len(value) > length else value
