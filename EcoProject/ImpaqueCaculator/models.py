from django.db import models
from django.contrib.auth.models import User


class Co2ProductionProfile(models.Model):
    """ The data aboute how much co2 the user emit by trensportation """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # store how many kg of co2 by day they produce givien there current mode of trensportation
    emition_in_one_day = models.IntegerField()

    # the number of litre consome eche 100km
    consomation_metric = models.FloatField()

    is_diesel = models.BooleanField()

    nomber_of_km_daylie = models.FloatField()

    def caculte_emiton_in_one_day(litre_by_100km, nomber_of_km_daylie, is_diesel):
        """
        dummy
        """
        if is_diesel:
            emsion_ratio = 2.64
        else:
            emsion_ratio = 2.392
        return nomber_of_km_daylie*litre_by_100km/100*emsion_ratio

    def __str__(self):
        return self.user.username
