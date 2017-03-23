from django.contrib.auth.models import User, Group
from .models import GetClient
from rest_framework import serializers

#Serializer class converts the model to json data
#this allows us to save data in a format we can transfer

# this class knows to convert the Client model
# this is the one that comes back as if its a json object
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetClient
        fields = ('client_name', 'client_phone', 'client_address') #, 'log_no', 'driver_no', 'dob', 'no_of_lessons', 'comments', 'balance')
        #fields = '__all__'





# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
#

