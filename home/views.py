from django.shortcuts import render

# Create your views here.
from home.models import Slider, About


def home(request):
    sliders = Slider.objects.all()
    about = About.objects.first()
    contex = {'sliders':sliders,'about':about}
    return  render(request,'home/home.html',contex)

