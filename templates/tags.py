from django.http import HttpRequest
from django import template
from django.urls import reverse


register = template.Library()


@register.simple_tag
def getUrl(request, name=None):
    type = 'http://'
    if name is not None:
        return type + request.META['HTTP_HOST'] + reverse(name)
    else:
        return type + request.META['HTTP_HOST']


