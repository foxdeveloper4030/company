from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, Release


# Create your views here.
def index(request):
    releases = Release.objects.all()
    context = {'release': releases}
    return render(request, 'product/product.html', context)

def show(request,id):
    release = Release.objects.get(id=id)
    return