# Imports standard libraries
#...

# Imports core Django libraries
#...

# Imports third-party libraries
from rest_framework import serializers


# Imports from your apps
from .models import Reading



class ReadingSerializer(serializers.ModelSerializer):
    """ Serializer For Reading To show all fields and update it """

    class Meta:
        model = Reading
        fields  = '__all__'

class ReadingAPISerializer(serializers.ModelSerializer):
    """ Serializer For Reading To list heart_rate, breathing_rate, trembling_rate"""

    class Meta:
        model = Reading
        #fields = '__all__'
        fields  = ['heart_rate', 'breathing_rate', 'trembling_rate']
