from django.shortcuts import render
from .models import GetClient



def home(request):
    clientdata = GetClient.objects.order_by('client_name')  # clientdata will be a list of all the clients
    return render(request, 'getdata/home.html', {'getclients': clientdata}) #dsad
