from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]