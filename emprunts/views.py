from django.shortcuts import render
from .models import Emprunt

def liste_emprunt(request):
    emprunts = Emprunt.objects.all()
    return render (request, 'emprunt/list.html' ,{"emprunts" : emprunts })
