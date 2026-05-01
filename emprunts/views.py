from django.shortcuts import render,redirect

from .forms import EmpruntForm

def ajouter_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = EmpruntForm()
        return render(request,'ajouter_emprunt.html',{"form":form})
    else:
        form =EmpruntForm()
        return render(request,'emprunts/ajouter_emprunt.html',{"form":form})

def confirmer_emprunt(request):
    data =request.session.get ('emprunt_data')
    if data:
        form =EmpruntForm(data)
        if form.is_valid():
            form.save()
            del request.session['emprunt_data']
            return redirect('liste_emprunts')
    return redirect('ajouter_emprunt')