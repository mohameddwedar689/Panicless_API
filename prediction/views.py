from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import features
from .serializers import featuresSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


# Create your views here.

class FeatureView(viewsets.ModelViewSet):
    queryset = features.objects.all()
    serializer_class = featuresSerializers
    
@api_view(["POST" , "GET"])
def FeaturesView(request):
    try:
        model = joblib.load("D:\Panicless-Prediction\prediction_api\model.pkl")
        data = request.data
        unit = np.array(list(data.values()))
        unit = unit.reshape(1 , -1)
        prediction = model.predict(unit)
        
        if prediction == 1:
            return Response({"message":"You Should Consider Going To The Doctor"})
        elif prediction == 0:
            return Response({"message":"We Believe That There is No serious Concern For You To See The Doctor"})
    except ValueError as e:
		    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
