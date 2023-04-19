from django.db import models

# Create your models here.
class Reading(models.Model):
    """models for reading app """
    user           = models.OneToOneField('account.User', related_name='reading', on_delete=models.CASCADE, verbose_name='username')
    heart_rate     = models.PositiveIntegerField()
    breathing_rate = models.PositiveIntegerField()
    trembling_rate = models.PositiveIntegerField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)