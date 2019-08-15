from django.db import models

# Create your models here.
from django.db import models
from django.db.models import F


class Co2EmisonProfile(models.Model):
    """ store the data abaut a user curent emison
     of co2 related to there curent means of transport"""

    # the amount of conbustibe consom in litre
    consumption_metric = models.FloatField()

    # the montly number of km travel
    distance_travele = models.FloatField()

    # if true, the vecule is using diasel
    is_diesel = models.BooleanField()

    # the nomber of kg of co2 emited
    co2_emission_metric = models.FloatField(blank=True)

    class Meta:
        app_label = 'EcoProject'

    # performing the fellowing cacule:
    # D*C/100*Er = Et
    # where:
    #  D is the number of km travele montly
    #  C is the nomber of litre burn for eche km
    #  Er is the emison ration
    #  witche is:
    #       for Diesel: 2.64 kg of co2/l
    #       for Essence: 2.39 kg of co2/l
    #   Et is the number of kg of co2 emited
#    def cuculect_emison(self):
#        self
