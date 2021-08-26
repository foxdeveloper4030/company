import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import FileExtensionValidator
from xdg.Mime import magic
import os
from .models import Project, File
from datetime import time
import re
import hashlib


class ProjectValidations(forms.Form):
    name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    # type = forms.CharField(required=True)
    order_by_fname = forms.CharField(required=True)
    order_by_lname = forms.CharField(required=True)
    address = forms.CharField(required=True)
    order_by_tel = forms.CharField(required=True)
    website = forms.CharField(required=False)
    company = forms.CharField(required=False)
    file = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def clean_order_by_tel(self):
        pattern = r"[09]{9}"
        if re.match(pattern, self.cleaned_data['order_by_tel']):
            raise forms.ValidationError("تلفن اشتباه است.")
        for project in Project.objects.filter(order_by_tel=self.cleaned_data['order_by_tel']):
            if self.cleaned_data['order_by_tel'] == project.order_by_tel:
                raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است!")
