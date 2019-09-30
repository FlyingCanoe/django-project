from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F


class Co2EmisonProfile(models.Model):
    """ store the data abaut a user curent emison
     of co2 related to there curent means of transport"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # the amount of conbustibe consom in litre/100km
    consumption_metric = models.IntegerField()

    # if true, the vecule is using diasel
    DIESEL = 'DI'
    ESENCE = 'ES'
    COMBUSTIBLE_CHOICES = [
        (DIESEL, 'diesel'),
        (ESENCE, 'esence'),
    ]
    is_diesel = models.CharField(
        max_length=2,
        choices=COMBUSTIBLE_CHOICES,
        default=ESENCE,
    )

    def __str__(self):
        return("{} co2 emison profile".format(self.user.username))


class Engagement(models.Model):
    """ store a spesifique engament of a user"""
    profile = models.ForeignKey(Co2EmisonProfile, on_delete=models.CASCADE)

    # the duration of the engement in day
    duration = models.IntegerField(help_text="durée de l'engament en jour",)

    # the distance traveled in the engament
    distance = models.IntegerField(
        help_text="nombre de km parcourue durent l'engament"
    )

    emison_metric = models.IntegerField()

    def cuculet_emison(self):
        if Co2EmisonProfile.is_diesel == 'ES':
            tau_de_conversion = 1
        else:
            tau_de_conversion = 2

        self.emison_metric = 0

        self.emison_metric = self.profile.consumption_metric * \
            tau_de_conversion * self.distance
        self.save

        try:
            globalvar = GlobalEmisonMetric.objects.get(name='global')
        except:
            obj = GlobalEmisonMetric(
                name='global',
                emison_metric=0,
            )
            obj.save
            globalvar = GlobalEmisonMetric.objects.get(name='global')
        finally:
            print(globalvar.emison_metric)
            globalvar.add(self.emison_metric)
            globalvar.save
            print(globalvar.emison_metric)


class GlobalEmisonMetric(models.Model):
    name = models.TextField()
    emison_metric = models.IntegerField()

    def add(self, add):
        self.emison_metric += add
