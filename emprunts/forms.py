from django import forms
from .models import Emprunt
class EmpruntForm(forms.ModelForm):
    class Meta :
        model = Emprunt
        fields= ['ref_livre','adherent']


class EnregistrementRetourEmprunt(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['date_retour','remarque']
        widgets = {
            'date_retour' : forms.DateInput(attrs={
                'class' : 'form-control'
            }),
            'remarque' : forms.Textarea(attrs={
                'class' : 'form-control'
            })
        }