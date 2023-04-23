# Imports standard libraries
#...

# Imports third-party libraries
from rest_framework import serializers

# Imports from your apps
from .models import Reading


class ReadingSerializer(serializers.ModelSerializer):
    """ Serializer For Reading To show all fields and update it """

    class Meta:
        # assuming the JSON object is stored in a string variable called json_str
        model = Reading
        fields  = '__all__'

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        """to get user from request and add to validation data"""
        user = self.context["request"].user
        validated_data.update(user=user)
        return super().create(validated_data)




class ReadingDetailsSerializer(serializers.ModelSerializer):
    """ Serializer For Reading To list heart_rate, breathing_rate, trembling_rate
        For update and Retrieve
    """
    class Meta:
        model = Reading

        fields  = ['id', 'heart_rate', 'breathing_rate', 'trembling_rate']

        extra_kwargs = {
            'user': {'read_only': True}
        }