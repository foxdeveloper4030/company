from datetime import time
from os import mkdir
from random import randint


import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from home.models import Slider, About, Service
from .models import Project, Release, File, Category, Company
from . import forms
import hashlib
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    releases = Release.objects.all()
    context = {'release': releases}
    return render(request, 'product/product.html', context)


def show(request, id):
    release = Release.objects.get(id=id)
    return


def upload_file(file, name):
    ff = open(name, 'wb+')
    for line in file.chunks():
        ff.write(line)
    ff.close()


def order_project(request):
    if request.method == 'GET':
        return render(request, 'product/product.html',)
    if request.method == 'POST':

        if forms.ProjectValidations(request.POST, request.FILES).is_valid():
            project = Project()
            project.name = request.POST['name']
            project.title = request.POST['title']
            project.description = request.POST['description']
            # project.type = request.POST['type']
            project.order_by_fname = request.POST['order_by_fname']
            project.order_by_lname = request.POST['order_by_lname']
            project.address = request.POST['address']
            project.order_by_tel = request.POST['order_by_tel']
            project.website = request.POST['website']
            project.company = request.POST['company']
            project.save()
            if 'file' in request.FILES:
                file = File()
                file.name = project.name
                file.title = project.title
                file.project = project
                rand = randint(0, 100000)
                file_name = 'public/files' + '/' + str(hashlib.md5(str(rand).encode('utf-8')).hexdigest()) + \
                            request.FILES['file'].name
                upload_file(request.FILES['file'], file_name)
                file.address = file_name
                file.save()
                message = {'message':{'text':'ok'}}
                return render(request, 'product/product.html',
                              {'message': {'text': "ثبت نام شما انجام شد. به زودی با شما تماس خواهیم گرفت."}})


        else:

            return render(request, 'product/product.html', {'form': forms.ProjectValidations(request.POST,request.FILES).errors,
                                                            'message': {'text': "لطفا خطا های زیر را برطرف کنید."}})
