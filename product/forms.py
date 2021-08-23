import datetime

from  django import forms
from django.core.exceptions import ValidationError
from xdg.Mime import magic
import os
from .models import Project, File
from datetime import time
import re

class ProjectValidations(forms.Form):
    name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    type = forms.CharField(required=True)
    order_by_fname = forms.CharField(required=True)
    order_by_lname = forms.CharField(required=True)
    address = forms.CharField(required=True)
    order_by_tel = forms.CharField(required=True)
    website = forms.CharField(required=False)
    company = forms.CharField(required=False)
    file = forms.FileField(required=False)

    def clean_order_by_tel(self):
        pattern = r"[09]{9}"
        if re.match(pattern, self.cleaned_data['order_by_tel']):
            raise forms.ValidationError("تلفن اشتباه است.")
        for project in Project.objects.filter(phone_number=self.cleaned_data['order_by_tel']):
            if self.cleaned_data['order_by_tel'] == project.phone_number:
                raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است!")

    def validate_file(self):
        class Meta:
            model = File
            fil = os.path.splitext(self.file.name)[1]
            valid_extensions = ['.pdf', '.jpg', 'png']
            if not fil.lower() in valid_extensions:
                raise forms.ValidationError(' لطفا فایل')
  # def clean(self):
#     if not "pdf" in magic.form_file(self.file.url):
#         raise forms.ValidationError("لطفا فایل را با پسوندpdf وارد کنید")



# def __unicode__(self):
#     return self.fil