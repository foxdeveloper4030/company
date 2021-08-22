from  django import forms
from  .models import Project
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
    state = forms.IntegerField(required=True)
    website = forms.CharField(required=True)
    company = forms.CharField(required=True)

    def clean_order_by_tel(self):
        pattern = r"[09]{9}"
        if re.match(pattern, self.cleaned_data['order_by_tel']):
            raise forms.ValidationError("تلفن اشتباه است.")
        for project in Project.objects.filter(phone_number=self.cleaned_data['order_by_tel']):
            if self.cleaned_data['order_by_tel'] == project.phone_number:
                raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است!")
