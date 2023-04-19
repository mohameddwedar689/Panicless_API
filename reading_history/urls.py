from django.urls import path
from reading_history.views import CreateReadingAPI, ListReadingAPI, UpdateReadingAPI, DeleteReadingAPI,RetrieveReadingAPI
urlpatterns = [
    path("create-reading/", CreateReadingAPI.as_view()),
    path("list-reading/", ListReadingAPI.as_view()),
    path("update-reading/<int:pk>/", UpdateReadingAPI.as_view()),
    path("delete-reading/<int:pk>/", DeleteReadingAPI.as_view()),
    path("retrieve-reading/<int:pk>/", RetrieveReadingAPI.as_view()),
]