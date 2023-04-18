from django.db import models

# Create your models here.
class account(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    trustNumber = models.CharField(max_length=11)