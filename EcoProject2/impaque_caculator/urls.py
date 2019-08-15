from django.urls import path

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('mon_impaque', views.impaque_detail_view, name='DetailView'),
    path('caculateur_impaque', views.impaque_create_view, name='CreateView'),
]
