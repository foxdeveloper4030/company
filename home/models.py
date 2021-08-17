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
        css = {
            'all': ('https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',)
        }
        js = ('assets/js/ckeditor/ckeditor.js', 'assets/js/ckeditor/ckeditor_init.js')

    form = MyModelAdminForm


class Gallery(models.Model):
    img = models.ImageField(upload_to='public/img/galleries')
    name = models.CharField(max_length=250)


class Service(models.Model):
    img = models.ImageField(upload_to='public/img/services')
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)


class ModelServiceAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': forms.Textarea(attrs={'id': 'Text'})
        }
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',)
        }
        js = ('assets/js/ckeditor/ckeditor.js', 'assets/js/ckeditor/ckeditor_init.js')

    form = ModelServiceAdminForm
class Employment(models.Model):
    fist_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    description = models.TextField()

