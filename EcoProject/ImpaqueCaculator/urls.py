from django.urls import path

from . import views

urlpatterns = [
    path('MonImpaque', views.ProfileCreateView),
]
