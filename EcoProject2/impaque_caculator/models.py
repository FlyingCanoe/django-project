from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F


class Co2EmisonProfile(models.Model):
    """ store the data abaut a user curent emison
     of co2 related to there curent means of transport"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # the amount of conbustibe consom in litre
    consumption_metric = models.FloatField()

    # the montly number of km travel
    distance_travele = models.FloatField()

    # if true, the vecule is using diasel
    is_diesel = models.BooleanField()

    # the nomber of kg of co2 emited
    co2_emission_metric = models.FloatField(blank=True, null=True)

    # performing the fellowing cacule:
    # D*C/100*Er = Et
    # where:
    #  D is the number of km travele montly
    #  C is the nomber of litre burn for eche km
    #  Er is the emison ration
    #  witche is:
    #       for Diesel: 2.64 kg/l
    #       for Essence: 2.39 kg/l
    #   Et is the number of kg of co2 emited
    def cuculect_emison(self):
        """caculate the curent montly emison of co2 of the user"""

        if self.is_diesel == True:
            # since the emison ratio of diesel is 2.64 kg/l
            Er = 2.64
        else:
            # since the emison ratio of essence is 2.39/l
            Er = 2.39

        d = F('distance_travele')

        c = F('consumption_metric')
        self.co2_emission_metric = d*c/100*Er
        self.save()
        self.refresh_from_db()
