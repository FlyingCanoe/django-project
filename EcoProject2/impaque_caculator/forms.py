from django import forms
from django.core.exceptions import ValidationError


class ImpaqueCreateForm(forms.Form):

    nombre_de_litre_au_100_km = forms.FloatField()
    nombre_de_km_parcourue_par_jour = forms.FloatField()
    is_diesel = forms.BooleanField(
        required=False, label='est que votre vecule utilise du diesel')

    def clean_nombre_de_litre_au_100_km(self):
        data = self.cleaned_data['nombre_de_litre_au_100_km']

        # check if the consomation metric is positif
        if data < 0:
            raise ValidationError(_('entrer des valeur positif'))

        return data

    def clean_nombre_de_km_parcourue_par_jour(self):
        data = self.cleaned_data['nombre_de_km_parcourue_par_jour']

        # check if the consomation metric is positif
        if data < 0:
            raise ValidationError(_('entrer des valeur positif'))

        return data
