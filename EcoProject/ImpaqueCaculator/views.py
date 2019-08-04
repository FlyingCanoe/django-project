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
            profile = Co2ProductionProfile()
            profile.user = request.user
            profile.emition_in_one_day = form.cleaned_data['emition_in_one_day']
            profile.save()
            return HttpResponseRedirect('/testd/')

    else:
        # check if user alredy has a profile model
        try:
            Co2ProductionProfile.objects.get(user=request.user)

    # if he do not have one he is send to form to creat one
        except:
            form = Co2ProductutionForm
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
