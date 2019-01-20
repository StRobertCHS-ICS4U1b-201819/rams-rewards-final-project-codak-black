from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def history(request):
    template_name = 'history/history.html'
    context = {
        "object_list":[12, 14, 232]
    }
    return render(request, template_name, context)