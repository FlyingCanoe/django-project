from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Co2ProductionProfile
from .forms import Co2ProductutionForm


@login_required
def ProfileCreateView(request):
    if request.method == 'POST':
        form = Co2ProductutionForm(request.POST)
        if form.is_valid():
            # create a empty profile
            profile = Co2ProductionProfile()

            # link the profile to the user
            profile.user = request.user

            # add directly ask field to the profile
            profile.is_diesel = form.cleaned_data['utilise_du_diasel']
            profile.emition_in_one_day = form.cleaned_data['emition_in_one_day']
            profile.nomber_of_km_daylie = form.declared_fields['nombre_de_km_parcouru_en_une_journée']

            # add inderecly ask field or field that nead forther caculation
            # profile.litre_by_km =
            profile.save()
            return HttpResponseRedirect('/testd/')

    else:
        # check if user alredy has a profile model
        try:
            Co2ProductionProfile.objects.get(user=request.user)

    # if he do not have one he is send to form to creat one
        except:
            form = Co2ProductutionForm()
            return render(request, 'ImpaqueCaculator/create.html', {'form': form})

        # oterwise we get him to see his impaque
        else:
            return HttpResponseRedirect(reverse('home'))


@login_required
def ProfileDetailViews(request):
    user = request.user
    try:
        profile = Co2ProductionProfile.objects.get(user=user)
    except:
        return HttpResponseRedirect('initalise')
    template = loader.get_template('ImpaqueCaculator/detail.html')
    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'ImpaqueCaculator/detail.html', context)
