
from django.contrib import admin
from django.urls import path, include
from .views import index, show, order_project

urlpatterns = [
    path('', index, name='products.index'),
    path('/project', order_project, name="order_project")
]
