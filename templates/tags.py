from django.http import HttpRequest
from django import template
from django.urls import reverse
from home import models

register = template.Library()


@register.simple_tag
def getUrl(request, name=None):
    type = 'http://'
    if name is not None:
        return type + request.META['HTTP_HOST'] + reverse(name)
    else:
        return type + request.META['HTTP_HOST']


@register.simple_tag
def social():
    social = models.Social.objects.all()
    return social
