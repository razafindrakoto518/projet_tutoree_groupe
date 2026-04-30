from datetime import timedelta, datetime

from django.db import models
from livres.models import Livre
from adherents.models import Adherent
from django.contrib.auth.models import User

STATUT = [
    ('En retard', 'En retard'),
    ('Retourné', 'Retourné')
]
class Emprunt(models.Model):
    ref_livre = models.ForeignKey(Livre, on_delete=models.CASCADE, limit_choices_to={
        'quantite__gte' :1 
    })
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    bibliothecaire = models.OneToOneField(User,on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_limite = models.DateField(default=datetime.now() + timedelta(days=15))
    date_retour = models.DateField(null=True)
    statut = models.CharField(choices=STATUT)
    remarque = models.TextField()