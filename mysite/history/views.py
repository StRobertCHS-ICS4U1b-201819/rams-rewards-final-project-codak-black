from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import History

def history(request):
    template_name = 'history/history.html'
    queryset = History.objects.all( )
    context = {
        "object_list":queryset
    }
    return render(request, template_name, context)