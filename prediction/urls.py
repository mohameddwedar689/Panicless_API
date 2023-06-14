from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('prediction_api' , views.FeatureView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/' , views.FeaturesView)
]