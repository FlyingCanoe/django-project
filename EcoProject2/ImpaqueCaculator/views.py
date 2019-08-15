from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import ImpaqueCreateForm
from .models import Co2EmisonProfile


@login_required
def impaque_detail_view(request):
    """ dummy """
    return HttpResponse('helo word')


@login_required
def impaque_create_view(request):
    """ create co2 emison profile if it don't alrediy existe """

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ImpaqueCreateForm(request.POST)

        if form.is_valid():
            profile = Co2EmisonProfile()
            profile.consumption_metric = form.cleaned_data['nombre_de_litre_au_100_km']
            profile.distance_travele = form.cleaned_data['nombre_de_km_parcourue_par_jour']
            profile.is_diesel = form.cleaned_data['is_diesel']
            profile.save()

            return HttpResponseRedirect(reverse('DetailView'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ImpaqueCreateForm()
        context = {'form': form}
        return render(request, 'create.html', context)
