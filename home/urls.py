
from django.contrib import admin
from django.urls import path,include
from .views import home,adminGallery
urlpatterns = [
     path('',home,name='home'),
    path('admin/gallery/show',adminGallery,name='admin.gallery.get'),
]
