from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import FormulaireAuthentification

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="authentification/connexion.html",
                                            authentication_form=FormulaireAuthentification), name="seConnecter"),

]
