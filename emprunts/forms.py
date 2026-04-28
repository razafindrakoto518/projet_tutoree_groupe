
from django import forms
from .models import Emprunt
class EmpruntForm(forms.ModelForm):
    class Meta :
        model = Emprunt
        fields =['ref_livre', 'adherent','date_retour','date_limite','statut']
        widget ={
            'ref_livre': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Livre'
            }),
            'adherent': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Empruteur'
            }),
            'date_emprunt': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Date Emprunt'
            }),
            'date_retour': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Date Retour'
            }),
            'date_limite': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Date Limite'
            }),
            'statut': forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Statut'
            }),

        }