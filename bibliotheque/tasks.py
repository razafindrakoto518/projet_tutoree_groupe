from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from emprunts.models import Emprunt


def envoyer_rappels():
    ajourd_hui = timezone.now().date()
    dans_3_jours = ajourd_hui + timedelta(days=3)

    emprunts_bientot = Emprunt.objects.filter(
        statut='Non retourné',
        date_limite=dans_3_jours
    )

    for emprunt in emprunts_bientot:
        send_mail(
            subject='Rappel- Retour de livre',
            message=f'Bonjour {emprunt.adherent.nom} {emprunt.adherent.prenom}, votre livre "{emprunt.ref_livre.titre}" doit être retounré dans 3 jours.',
            from_email='bibliotheque@email.com',
            recipient_list=[emprunt.adherent.email]
        )


    
    #Notification retard
    emprunts_retard = Emprunt.objects.filter(
        statut='Non retourné',
        date_limite__lt=ajourd_hui
    )


    for emprunt in emprunts_retard:
        send_mail(
            subject='Retard- Retour de livre',
            message=f'Bonjour {emprunt.adherent.nom} {emprunt.adherent.prenom}, votre livre "{emprunt.ref_livre.titre}" est en retard depuis le {emprunt.date_limite}.Veuillez le deposez auprès de la bibliothèque.',
            from_email='bibliotheque@email.com',
            recipient_list=[emprunt.adherent.email]
        )