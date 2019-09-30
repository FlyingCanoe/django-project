from django.contrib import admin

from .models import Engagement, Co2EmisonProfile, GlobalEmisonMetric

admin.site.register(Engagement)
admin.site.register(Co2EmisonProfile)
admin.site.register(GlobalEmisonMetric)
