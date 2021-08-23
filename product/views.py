import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Release
from . import forms


# Create your views here.
def index(request):
    releases = Release.objects.all()
    context = {'release': releases}
    return render(request, 'product/product.html', context)


def show(request, id):
    release = Release.objects.get(id=id)
    return


def order_project(request):
    if request.method == 'GET':
        return render(request, 'product/project.html')
    if request.method == 'POST':
        return JsonResponse(request.POST)
        if forms.ProjectValidations(request.POST).is_valid():
            project = Project()
            project.name = request.POST['name']
            project.title = request.POST['title']
            project.description = request.POST['description']
            project.type = request.POST['type']
            project.order_by_fname = request.POST['order_by_fname']
            project.order_by_lname = request.POST['order_by_lname']
            project.address = request.POST['address']
            project.order_by_tel = request.POST['order_by_tel']
            Project.website = request.POST['website']
            Project.company = request.POST['company']
            file = File()
            file.name = request.FILES['name']
            file.title = request.FILES['title']
            file.address = request.FILES['address']
            file.project = request.FILES['project']
            project.save()
            return render(request, 'product/project.html',
                          {'message': {'text': "سفارش شما ثبت شد."}})
        else:
            return render(request, 'home/employment.html', {'form': forms.ProjectValidations(request.POST).errors,
                                                            'message': {'text': "لطفا خطا های زیر را برطرف کنید."}})
