
from django import forms
from .models import Emprunt
class EmpruntForm(forms.ModelForm):
    class Meta :
        model=Emprunt
        fields=["ref_livre","adherent","date_emprunt","date_limite","date-retour"]