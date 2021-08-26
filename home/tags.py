
from django import template
from django.urls import reverse
from .models import Social

register = template.Library()

@register.simple_tag
def social():
    social = Social.objects.all()
    return social