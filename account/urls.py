from django.urls import include, path
from knox.views import LogoutAllView, LogoutView
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from account.views import CustomLoginView, UpdateProfileAPI


router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", CustomLoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("logoutall/", LogoutAllView.as_view()),
    path("updateprofile/<int:pk>/",UpdateProfileAPI.as_view()),
]
