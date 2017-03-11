from django.shortcuts import render
from .models import GetClient


def home(request):
    return render(request, 'getdata/home.html', {'getClients': GetClient}) #dsad
