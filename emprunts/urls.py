from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_emprunt, name= 'ajouter_emprunt'),
]