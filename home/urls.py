
from django.contrib import admin
from django.urls import path,include
from .views import home,adminGallery,employment
urlpatterns = [
    path('',home,name='home'),
    path('admin/gallery/show',adminGallery,name='admin.gallery.get'),
    path('employ/',employment,name='site.employment'),
    path('employ/store',employment,name='site.employment.store'),


]
