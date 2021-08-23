from django.http import JsonResponse, HttpResponse,Http404
from django.shortcuts import render
# Create your views here.
from home.models import Slider, About, Gallery, Service
from product.models import Release, Category, Company
from . import forms
from .models import Employment

def home(request):
    sliders = Slider.objects.all()
    about = About.objects.first()
    services = Service.objects.all()
    releases = Release.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.all()
    contex = {'sliders': sliders, 'about': about, 'services': services, 'releases': releases, 'categories': categories,
              'companies': companies}
    return render(request, 'home/home.html', contex)


def adminGallery(request):
    galleries = Gallery.objects.all()
    return render(request, 'admin/ShowGallery.html', {'galleries': galleries})


def employment(request):
    if request.method == 'GET':
         return render(request, 'home/employment.html')
    if request.method =='POST':
       if forms.EmployValidation(request.POST).is_valid():
           employ = Employment()

           employ.fist_name = request.POST['name']
           employ.last_name = request.POST['last_name']
           employ.email = request.POST['email']
           employ.phone_number = request.POST['tel']
           employ.description = request.POST['message']
           employ.save()
           return render(request, 'home/employment.html',
                         {'message':{'text':"ثبت نام شما انجام شد. به زودی با شما تماس خواهیم گرفت."}})
       else:
           return render(request, 'home/employment.html', {'form':forms.EmployValidation(request.POST).errors,'message':{'text':"لطفا خطا های زیر را برطرف کنید."}})
