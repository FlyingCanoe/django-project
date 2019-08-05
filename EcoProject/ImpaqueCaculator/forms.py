from . import models
from django import forms


class Co2ProductutionForm(forms.Form):
    litre_au_100_km = forms.FloatField()
    nombre_de_km_parcouru_en_une_journée = forms.FloatField()
    utilise_du_diasel = forms.BooleanField()
