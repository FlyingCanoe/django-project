from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

    # my app urls
    path('accounts/', include('accounts.urls')),
    path('', include('impaque_caculator.urls')),

    # django urls
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
