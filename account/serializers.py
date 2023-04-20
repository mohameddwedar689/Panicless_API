# Imports standard libraries
# ...

# Imports core Django libraries
from django.contrib.auth import authenticate
from django.conf import settings
from django.db.models import Q

# Imports third-party libraries
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from rest_framework import serializers
from rest_framework import status

# Imports from your apps
from .models import Account
from Order.serializers import OrderServiceSerializer





class RegisterSerializer(serializers.ModelSerializer):
    """Serializer For Register """
    password = PasswordRegisterField(style={'input_type': 'password'}, min_length=6, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password', 'photo', 'fcm_token')

        extra_kwargs = {
            'password': {
                'style': {'input_type': 'password'}
            }
        }

    def to_representation(self, instance):
        instance.photo = 'media/' + str(instance.photo)
        return super().to_representation(instance)

    # overide create
    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        return account


class LoginSerializer(serializers.ModelSerializer):
    """Serializer For Login """
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Account
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        # validate user data and authenticate it to login

    def validate(self, data):
        user = authenticate(**data)
        # check if login user is active and profile type if driver
        if user and user.is_active:
            return user
        # need to update raise
        raise ValueError('Invalid Credentials.')

