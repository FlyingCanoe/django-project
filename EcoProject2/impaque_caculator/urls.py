from django.urls import path

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('mon_profile', views.impaque_detail_view, name='DetailView'),
    path('createur_de_profile', views.impaque_create_view, name='CreateView'),
    path('mes_engament', views.engagement_list_view, name='EngementListView'),
    path('prendre_engament', views.EngamintCreateView.as_view(),
         name='EngamentCreateView')
]
