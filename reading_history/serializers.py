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
