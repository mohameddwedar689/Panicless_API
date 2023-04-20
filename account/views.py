# Imports standard libraries
from datetime import timedelta, datetime

# Imports core Django libraries
#...

# Imports third-party libraries
from rest_framework import generics,permissions
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework.views import APIView
from knox.auth import AuthToken, TokenAuthentication
from knox.views import LogoutView, LogoutAllView

# Imports from your apps
from account.models import Account
#from Account.serializers import  RegisterSerializer, LoginSerializer


class RegisterAPI(generics.GenericAPIView):
    """ To register Endpoint """
    serializer_class = RegisterSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        '''
        API that register a user and create account for user
        '''
        # serialize data in request by register serializer
        account_serializer = self.get_serializer(data=request.data)
        if account_serializer.is_valid(raise_exception=True):
            account_serializer.save()
        return Response(account_serializer.data, status=status.HTTP_201_CREATED)



class LoginAPI(generics.GenericAPIView):
    """ To login Endpoint """
    serializer_class       = LoginSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes     = (permissions.AllowAny,)

    def post(self, request):
        '''
        API that login a user with token
        '''
        account_serializer = self.get_serializer(data=request.data)
        try:
            if account_serializer.is_valid(raise_exception=True):
                account_ = account_serializer.validated_data
                account  = AccountSerializer(account_).data
                account['token'], account['expire']  = generate_token(account_)
            return Response(account, status=status.HTTP_200_OK)
        except ValueError as er:
            return Response("Invalid Credentials.",status=status.HTTP_401_UNAUTHORIZED)



class UpdateProfileAPI(generics.UpdateAPIView):
    """ To Update User Profile Endpoint """
    permission_classes = (AllowAny,)
    queryset = Account.objects.all()
    serializer_class = UpdateProfile