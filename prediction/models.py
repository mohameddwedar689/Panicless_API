from django.db import models

# Create your models here.

class features(models.Model):
    nervous = models.BooleanField()
    panic = models.BooleanField()
    breathing = models.BooleanField()
    sweating = models.BooleanField()
    trouble_consentrate = models.BooleanField()
    trouble_sleep = models.BooleanField()
    trouble_work = models.BooleanField()
    hopelessness = models.BooleanField()
    anger = models.BooleanField()
    over_react = models.BooleanField()
    eating = models.BooleanField()
    thought = models.BooleanField()
    tired = models.BooleanField()
    friend = models.BooleanField()
    social_media = models.BooleanField()
    weight_gain = models.BooleanField()
    material = models.BooleanField()
    introvert = models.BooleanField()
    stressful_memory = models.BooleanField()
    nightmares = models.BooleanField()
    avoid_people = models.BooleanField()
    negative = models.BooleanField()
    trouble_concentrating = models.BooleanField()
    blaming_yourself = models.BooleanField()
    