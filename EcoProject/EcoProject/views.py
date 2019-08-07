from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = 'home.html'


def impaque_detail_view(request):
    """ dummy """
    return HttpResponse('helo word')


def impaque_create_view(request):
    """ dummy """
    return HttpResponse('helo word')
