from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .forms import ImpaqueCreateForm
from .models import Co2EmisonProfile


@login_required
def impaque_detail_view(request):
    """ dummy """
    # if the user do not have a profile we send him to create it
    try:
        Co2EmisonProfile.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('CreateView'))

    profile = Co2EmisonProfile.objects.get(user=request.user)
    context = {'emison_metric': profile.co2_emission_metric}
    return render(request, 'detail.html', context=context)


@login_required
def impaque_create_view(request):
    """ create co2 emison profile if it don't alrediy existe """

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # if the user allredy as a profile we redirect him to see is profile
        try:
            Co2EmisonProfile.objects.get(user=request.user)
        except:
             # Create a form instance and populate it with data from the request
            form = ImpaqueCreateForm(request.POST)

            if form.is_valid():
                user = request.user

                profile = Co2EmisonProfile()
                profile.is_diesel = form.cleaned_data['is_diesel']
                profile.consumption_metric = form.cleaned_data['nombre_de_litre_au_100_km']
                profile.distance_travele = form.cleaned_data['nombre_de_km_parcourue_par_jour']*30
                profile.user = user
                profile.save()
                profile.cuculect_emison()

                return HttpResponseRedirect(reverse('DetailView'))

        else:
            return HttpResponseRedirect(reverse('DetailView'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ImpaqueCreateForm()
        context = {'form': form}
        return render(request, 'create.html', context)


def home(request):
    sum = Co2EmisonProfile.objects.aggregate(Sum('co2_emission_metric'))

    context = {'sum': sum['co2_emission_metric__sum']}
    return render(request, 'home.html', context)
