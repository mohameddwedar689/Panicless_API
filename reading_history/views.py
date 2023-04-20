# Imports standard libraries
#...

# Imports core Django libraries
#...

# Imports third-party libraries
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response

# Imports from your apps
from .serializers import ReadingSerializer, ReadingDetailsSerializer
from reading_history.models import Reading



class CreateReadingAPI(generics.CreateAPIView):
    """ To Create Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset           = Reading.objects.all()
    serializer_class   = ReadingSerializer


class ListReadingAPI(generics.ListAPIView):
    """ To Create Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset           = Reading.objects.all()
    serializer_class   = ReadingSerializer

    def get_queryset(self):
        print(self.request.user, "--------------")
        queryset = Reading.objects.filter(user=self.request.user)
        return queryset


class DeleteReadingAPI(generics.DestroyAPIView):
    """ To Delete Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset           = Reading.objects.all()
    serializer_class   = ReadingSerializer


class UpdateReadingAPI(generics.UpdateAPIView):
    """ To Update Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset           = Reading.objects.all()
    serializer_class   = ReadingDetailsSerializer


class RetrieveReadingAPI(generics.RetrieveAPIView):
    """ To Retrieve Reading Endpoint """
    permission_classes = (IsAuthenticated,)
    queryset           = Reading.objects.all()
    serializer_class   = ReadingDetailsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Reading.objects.filter(user=self.request.user).last
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

