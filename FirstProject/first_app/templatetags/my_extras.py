from django import template

register = template.Library()

@register.filter(name='myupper')
def myupper(value, arg):
    """
    This this makes the first arg number of letter uppercase
    """
    return value.replace(value[:arg], value[:arg].upper())
