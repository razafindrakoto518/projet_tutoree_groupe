from django.shortcuts import render,redirect

from .forms import EmpruntForm

def ajouter_emprunt(request):
    form = EmpruntForm (request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_emprunt')
    return render(request, 'emprunts/formulaire.html',{'form': form})