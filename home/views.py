from django.shortcuts import render

# Create your views here.
from home.models import Slider, About, Gallery, Service
from product.models import Release


def home(request):
    sliders = Slider.objects.all()
    about = About.objects.first()
    services = Service.objects.all()
    releases = Release.objects.all()
    contex = {'sliders': sliders, 'about': about,'services':services,'releases':releases}
    return render(request, 'home/home.html', contex)


def adminGallery(request):
    galleries = Gallery.objects.all()
    return render(request,'admin/ShowGallery.html',{'galleries':galleries})
