# Imports standard libraries
#...

# Imports core Django libraries
#...

# Imports third-party libraries
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

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
    ordering_fields = ['id']
    ordering = ['-id']

    def get_queryset(self):
        """ override on get queryset function to filter user in request """
        queryset = Reading.objects.filter(user=self.request.user)
        return queryset

    # def get_paginated_response(self, data):
    #     """ To Remove count, next, previous from response """
    #     return Response(data)


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



class RetrieveReadingAPI(viewsets.ModelViewSet):
    """ another way To get last reading in list of reading object """
    queryset = Reading.objects.all()
    serializer_class = ReadingDetailsSerializer

    def list(self, request):
        """ override on list function and get lat element in the list """
        queryset = Reading.objects.filter(user=self.request.user)
        serializer = self.get_serializer(queryset.last(), many=False)
        return Response(serializer.data)


# class RetrieveReadingAPI(viewsets.ModelViewSet):
#     """ To get last reading in list of reading object """
#     queryset = Reading.objects.all()
#     serializer_class = ReadingDetailsSerializer
#
#     def list(self, request):
#         """ override on list function and get lat element in the list """
#         queryset = Reading.objects.filter(user=self.request.user)
#         serializer = self.get_serializer(queryset.order_by('-id')[:1], many=True)
#         return Response(serializer.data)

