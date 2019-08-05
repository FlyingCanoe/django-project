from django.test import TestCase

from.models import Co2ProductionProfile


class Co2ProductionProfileTests(TestCase):

    # to caculate the emiton of a car you have to make the following cacule
    # D*C/100*Er
    # where:

    # D is the number of km traveled

    # C is the consumption in L/100 km

    # Er is emission ratio that is the nomber of kg of co2 emit by litre of combustibe
    # for diesel it is 2.64 co2/L
    # essence 2.392 co2/l

    # in that case we are caculation 5*2/100*2.64 = 0.264
    def caculte_emiton_in_one_day_with_diesel(self):
        C = 2
        D = 5

        self.assertIs(Co2ProductionProfile.caculte_emiton_in_one_day(
            C, D, is_diesel=True), 0.264)

    # in that case we are caculating 5*2/100*2.392 =
    def caculte_emiton_in_one_day_with_essence(self):
        C = 2
        D = 5

        self.assertIs(Co2ProductionProfile.caculte_emiton_in_one_day(
            C, D, is_diesel=False))
