from django.db import models

# Create your models here.
class history(models.Model):
    heartRate = models.IntegerField(max_length=10)
    breathingRate = models.CharField(max_length=50)
    tremblingRate = models.CharField(max_length=50)
    dataTime = models.DateTimeField()
    