from django.db import models


class Co2EmisonProfile(models.Model):
    """ store the data abaut a user curent emison
     of co2 related to there curent means of transport"""

    # the amount of conbustibe consom in litre
    consumption_metric = models.FloatField()

    # if true, the vecule is using diasel
    is_diesel = models.BooleanField()

    # the montly number of km travel
    distance_travele = models.FloatField()

    # the nomber of kg of co2 emited
    co2_emission_metric = models.FloatField()
