from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'teacher/home.html')

def contact(request):
    return render(request, 'teacher/basic.html',{'content':['If you '
     'would like to contact me, please email me.','hskinsley@gmail.com']})