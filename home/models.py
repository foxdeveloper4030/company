from django.contrib import admin
from django.contrib.admin.forms import forms
from django.db import models


# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/sliders/img')
    alt = models.CharField(max_length=250)
    link = models.CharField(max_length=250)


class About(models.Model):
    Text = models.TextField()



class MyModelAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'Text': forms.Textarea(attrs={'id': 'Text'})
        }

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Media:
        js = ('assets/js/ckeditor.js','assets/js/admin.js')
    form = MyModelAdminForm


class Gallery(models.Model):
    img = models.ImageField(upload_to='public/img/galleries')
    name = models.CharField(max_length=250)
