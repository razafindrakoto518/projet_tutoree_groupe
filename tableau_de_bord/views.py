from django.shortcuts import render
from livres.models import Livre
from adherents.models import Adherent
from emprunts.models import Emprunt
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from dateutil.relativedelta import relativedelta


def index_dashboard(request):
    #Récuperation des quantité de livre par catégorie
    #.values('categorie') == regroupé par catégorie
    #.annotate(total_quantite=Sum('quantite')) == On additionne la valeur de l'attribut quantite de chaque categorie regroupé
    #Puis on arrange par catégorie
    quantite_par_categorie = Livre.objects.values('categorie').annotate(total_quantite=Sum('quantite')).order_by('categorie')
    #On regroupe les adhérents par fonction puis on crée une variable à la volé effectif total qui
    #contient l'effectif des adhérents groupés par fonction
    adherent_par_fonction = Adherent.objects.values('fonctions').annotate(effectif_total=Count('matricule'))
    
    
    #On recupère le nombre des emprunts du 7 mois passé
    #Définir un variable pour stocker la date de debut date ajourd'hui - 7 mois
    date_debut = timezone.now() - relativedelta(months=7)
    #__gt = greate than
    #__lte = less than or equal
    #__lt = less than
    #truncMonth = Tronque une date en ne gardant que l'année et les mois
    emprunt_par_mois = (
        Emprunt.objects.
        filter(date_emprunt__gte=date_debut)#gte = greater than or equal 'lookup django'
        .annotate(mois=TruncMonth('date_emprunt'))#On crée une variable temporaire mois , 
        .values('mois')#Regroupé par mois
        .annotate(total=Count('id'))#Crée une variable total pour stocker la total des emprunts en un mois 
        .order_by('mois')
    )


    retours_par_mois = (
        Emprunt.objects
        .filter(date_retour__isnull=False)#Filtrer les enregistrement où date_retour n'est pas vide
        .annotate(mois=TruncMonth('date_retour'))
        .values('mois')
        .annotate(total=Count('id'))
        .order_by('mois')
    )


    #Formatage pour le graphe emprunts/retours par mois
    #Formater les données pour faciliter leurs utilisation dans le graphe
    labels = []#Variable pour stocker les labels ['janvier', 'fevrier', ....]
    emprunts_data = []#Variable pour stocker les données pour emprunts
    retours_dict = {r['mois'].strftime('%b'): r['total']for r in retours_par_mois}

    for e in emprunt_par_mois:
        mois_label = e['mois'].strftime('%b')
        labels.append(mois_label)
        emprunts_data.append(e['total'])

    retours_data = [retours_dict.get(label, 0) for label in labels]
    print(labels)

    return render(request, 'tableau_de_bord/index.html')


