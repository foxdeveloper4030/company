from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# Create your views here.
from home.models import Slider, About, Gallery, Service
from product.models import Release, Category, Company


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
        return HttpResponse("lkjh")
    return render(request, 'home/employment.html')
