from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .forms import ImpaqueCreateForm, EngamentCreateForm
from .models import Co2EmisonProfile, Engagement, GlobalEmisonMetric
from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def impaque_detail_view(request):
    """ dummy """
    # if the user do not have a profile we send him to create it
    try:
        Co2EmisonProfile.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('CreateView'))

    profile = Co2EmisonProfile.objects.get(user=request.user)
    context = {
        'consumption_metric': profile.consumption_metric,
        'is_diesel': profile.is_diesel
    }

    return render(request, 'detail.html', context=context)


@login_required
def impaque_create_view(request):
    """ create co2 emison profile if it don't alrediy existe """

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = ImpaqueCreateForm(request.POST)

        if form.is_valid():
            user = request.user

            profile = Co2EmisonProfile()
            profile.consumption_metric = form.cleaned_data['consumption_metric']
            profile.user = user
            profile.save()

            return HttpResponseRedirect(reverse('DetailView'))

        else:
            return HttpResponseRedirect(reverse('DetailView'))

    # If this is a GET (or any other method) create the default form.
    else:
        # if the user allredy as a profile we redirect him to see is profile
        try:
            Co2EmisonProfile.objects.get(user=request.user)
        except:
            form = ImpaqueCreateForm()
            context = {'form': form}
            return render(request, 'create.html', context)
        else:
            return HttpResponseRedirect(reverse('DetailView'))


@login_required
def engagement_list_view(request):
    profile = Co2EmisonProfile.objects.get(user=request.user)
    engament_list = Engagement.objects.filter(profile=profile)
    context = {'engament_list': engament_list}
    return render(request, 'list.html', context)


class EngamintCreateView(LoginRequiredMixin, CreateView):
    model = Engagement
    fields = ['duration', 'distance']
    template_name = 'impaque_caculator/engagement_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.profile = Co2EmisonProfile.objects.get(user=self.request.user)
        obj.cuculet_emison()
        obj.save()
        return HttpResponseRedirect(reverse('EngementListView'))


def home(request):
    globalsum = GlobalEmisonMetric.objects.get(name='global')
    context = {'sum': globalsum.emison_metric}
    return render(request, 'home.html', context)
