from django.urls import path
from reading_history.views import CreateReadingAPI, UpdateReadingAPI, DeleteReadingAPI, RetrieveReadingAPI, ListReadingAPI
urlpatterns = [
    path("create-reading/", CreateReadingAPI.as_view()),
    path("list-reading/", ListReadingAPI.as_view()),
    path("update-reading/<int:pk>/", UpdateReadingAPI.as_view()),
    path("delete-reading/<int:pk>/", DeleteReadingAPI.as_view()),
    path("last-reading/", RetrieveReadingAPI.as_view({'get': 'list'})),
]