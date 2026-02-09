from django import template

register = template.Library()

@register.filter
def trim(value):
    """Remove leading and trailing whitespace"""
    if value:
        return value.strip()
    return value
