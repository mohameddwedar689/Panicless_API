from django.contrib.auth import get_user_model, login
from djoser.views import TokenCreateView
from knox.views import LoginView
from rest_framework import status
from rest_framework.response import Response

# Imports third-party libraries
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from account.serializers import UserLoginSerializers, UpdateProfile

User = get_user_model()


# ------------------- login -------------------------- #
class CustomLoginView(LoginView, TokenCreateView):
    serializer_class = UserLoginSerializers
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(response.data, status=status.HTTP_200_OK)


class UpdateProfileAPI(generics.UpdateAPIView):
    """ To Update User Profile Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UpdateProfile