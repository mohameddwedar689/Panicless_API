# Imports standard libraries
#...

# Imports core Django libraries
#...

# Imports third-party libraries
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

# Imports from your apps
from .serializers import ReadingSerializer, ReadingAPISerializer
from reading_history.models import Reading



class CreateReadingAPI(generics.CreateAPIView):
    """ To Create Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class ListReadingAPI(generics.ListAPIView):
    """ To List Reading Endpoint """
    serializer_class = ReadingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Reading.objects.all()

class ListReadingHBTAPI(generics.ListAPIView):
    """ To List list heart_rate, breathing_rate, trembling_rate Endpoint """
    serializer_class = ReadingAPISerializer
    permission_classes = (AllowAny,)
    queryset = Reading.objects.all()

class UpdateReadingAPI(generics.UpdateAPIView):
    """ To Update Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class DeleteReadingAPI(generics.DestroyAPIView):
    """ To Delete Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class RetrieveReadingAPI(generics.RetrieveAPIView):
    """ To Retrieve Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
