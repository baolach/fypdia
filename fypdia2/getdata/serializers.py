from .models import GetClient
from .models import GetLesson
from .models import GetLocation
from rest_framework import serializers

#Serializer class converts the model to json data
#this allows us to save data in a format we can transfer

# this class knows to convert the Client model
# this is the one that comes back as if its a json object
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetClient
        fields = '__all__'
        #fields = ('client_name', 'client_phone', 'client_address', 'log_no',
        # 'driver_no', 'dob', 'no_of_lessons', 'balance_due', 'comments', 'id')



class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetLesson
        #fields = ('lesson_name', 'lesson_date', 'lesson_time', 'lesson_location','lesson_comments')
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetLocation
        fields = ('id', 'type', 'coordinates','x', 'y')
        #fields = '__all__'

