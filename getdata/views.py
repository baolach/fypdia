from django.shortcuts import render
from .models import GetClient
import django.contrib.auth.models

#from rest_framework import viewsets
#from getdata.serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse


def index(request):
    all_entries = GetClient.objects.all()

    return HttpResponse(all_entries.values())


def home(request):
    clientdata = GetClient.objects.order_by('client_name')  # clientdata will be a list of all the clients
    return render(request, 'getdata/home.html', {'getclients': clientdata}) #dsad


'''
# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
# We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely
# organized as well as being very concise.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = django.contrib.auth.models.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = django.contrib.auth.models.Group.objects.all()
    serializer_class = GroupSerializer

# class ClientViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

'''