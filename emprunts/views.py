from django.shortcuts import render,redirect

from .forms import EmpruntForm

def ajouter_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
           #form.save()
            request.session['emprut_data']=request.POST
            return render(request,'emprunts/confirmation.html',{'form':form})
        else:
            form = EmpruntForm()
        return render(request,'ajouter_emprunt.html',{"form":form})
    else:
        form =EmpruntForm()
        return render(request,'emprunts/ajouter_emprunt.html',{"form":form})