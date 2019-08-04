from . import models
from django import forms


class Co2ProductutionForm(forms.Form):
    emition_in_one_day = forms.IntegerField()
