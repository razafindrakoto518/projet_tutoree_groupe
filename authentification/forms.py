from django.contrib.auth.forms import AuthenticationForm
from django import forms


#Créer une formulaire d'authentification qui hérite de AuthenticationForm
class FormulaireAuthentification(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)