
from django.contrib import admin
from django.urls import path,include
from .views import index, show

urlpatterns = [
    path('',index,name='products.index'),
    path('/show/<int:id>',show,name='products.show')
]
