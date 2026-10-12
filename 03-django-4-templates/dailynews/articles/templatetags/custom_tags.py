from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.filter(is_safe=True, needs_autoescape=True)
def display_length(value, autoescape=True):
    if len(value) == 0:
        return mark_safe("<p class='text-right'>%s result</p>" % (len(value)))
    else:
        return mark_safe("<p class='text-right'>%s results</p>" % (len(value)))


@register.filter()
def display_active(value, arg):
    print(value)
    print(arg)
    if value == arg:
        return "active"
    else:
        return ""


@register.filter()
def firstCap(value):
    str = ""
    arr = value.split(" ")
    for w in arr:
        str += w.capitalize() + " "
    return str


register.filter('display_length', display_length)
register.filter('display_active', display_active)
register.filter('firstCap', firstCap)
