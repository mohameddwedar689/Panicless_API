from django.contrib.auth import authenticate
from djoser.conf import settings
from djoser.serializers import (
    TokenCreateSerializer,
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from account.models import User


# ----------- just for user ---------- #
class UserSerializers(UserSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "firstName",
            "lastName",
            "email",
            "trustNumber",
            "is_active",
            "is_admin",
        )


# ----------- register ---------------- #
class UserCreateSerializers(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "firstName",
            "lastName",
            "email",
            "trustNumber",
            "image",
            "password",
        )

class UpdateProfile(serializers.ModelSerializer):
    """for update profile"""
    class Meta:
        model = User
        fields = ("firstName", "lastName", "image")

# ------------------- login --------------------- #
class UserLoginSerializers(TokenCreateSerializer):
    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not attrs:
            raise AuthenticationFailed(
                {"error": settings.CONSTANTS.messages.INVALID_CREDENTIALS_ERROR}
            )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if not self.user:
                raise AuthenticationFailed(
                    {"error": settings.CONSTANTS.messages.INVALID_CREDENTIALS_ERROR}
                )
            if not self.user.check_password(password):
                raise AuthenticationFailed(
                    {"error": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR}
                )
        if not self.user.is_active:
            raise AuthenticationFailed(
                {"error": settings.CONSTANTS.messages.INACTIVE_ACCOUNT_ERROR}
            )
        if self.user and self.user.is_active:
            attrs["user"] = self.user
            return attrs
        self.fail("default_case")
