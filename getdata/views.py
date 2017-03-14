
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView  # returns rpoper data
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer


from django.shortcuts import render
from .models import GetClient
import django.contrib.auth.models
#from rest_framework import viewsets
#from getdata.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse

# localhost:8000 - this just gets all the values
def index(request):
    all_entries = GetClient.objects.all()
    return HttpResponse(all_entries.values())


# localhost:8000/getdata - also outputs just the clients
def home(request):
    clientdata = GetClient.objects.order_by('client_name')  # clientdata will be a list of all the clients
    return render(request, 'getdata/home.html', {'getclients': clientdata})


# this either lists all clients or creates a new one
#
class ClientList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        clients = GetClient.objects.all()  # gets the clients to pass through the serializer
        serializer = ClientSerializer(clients, many=True)  # how many objects to be serialized
        return Response(serializer.data)  # the json data
        # return HttpResponse(clients.values())

    def post(self):
        return



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