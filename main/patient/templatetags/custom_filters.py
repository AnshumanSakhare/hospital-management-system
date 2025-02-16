from django import template
from builtins import getattr as built_in_getattr

register = template.Library()

@register.filter
def getattr(obj, attr):
    return built_in_getattr(obj, attr)
