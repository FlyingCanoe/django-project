from django.urls import path

from . import views


urlpatterns = [
    path('mon_impaque', views.impaque_detail_view, name='DetailView'),
    path('caculateur_impaque', views.impaque_create_view, name='CreateView'),
]
