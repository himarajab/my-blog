from django import template
register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()