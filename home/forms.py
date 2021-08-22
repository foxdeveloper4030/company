import re
from django import forms
from .models import Employment


class EmployValidation(forms.Form):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    tel = forms.CharField(required=True)
    message = forms.CharField(required=True)

    def clean_email(self):
        for employ in Employment.objects.filter(email=self.cleaned_data['email']):
            if self.cleaned_data['email'] == employ.email:
                raise forms.ValidationError("این ایمیل قبلا ثبت شده است!")

    def clean_tel(self):
        pattern = r"[09]{9}"
        if re.match(pattern,self.cleaned_data['tel']):
            raise forms.ValidationError("تلفن اشتباه است.")
        for employ in Employment.objects.filter(phone_number=self.cleaned_data['tel']):
            if self.cleaned_data['tel'] == employ.phone_number:
                raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است!")
