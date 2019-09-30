from django import forms
from django.core.exceptions import ValidationError
from .models import Co2EmisonProfile


class ImpaqueCreateForm(forms.Form):

    consumption_metric = forms.FloatField(
        label='nombre de litre au 100km'
    )
    combustible = forms.ChoiceField(
        choices=Co2EmisonProfile.COMBUSTIBLE_CHOICES, help_text='type de combustible'
    )

    def clean_consumption_metric(self):
        data = self.cleaned_data['consumption_metric']

        # check if the consomation metric is positif
        if data < 0:
            raise ValidationError(_('entrer des valeur positif'))

        return data


class EngamentCreateForm(forms.Form):
    duration = forms.IntegerField()
    distance = forms.IntegerField()

    def save(profile):
        Co2EmisonProfile(
            profile=profile,
            duration=duration,
            distance=distance,

        )
        profile = profile
