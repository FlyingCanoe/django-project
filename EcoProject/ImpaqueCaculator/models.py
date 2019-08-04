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

    def __str__(self):
        return self.user.username
