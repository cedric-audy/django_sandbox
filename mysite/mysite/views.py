from django.shortcuts import render
from django.http import Http404
from . import views

def index(request):
    return render(request, 'mysite/index.html')
