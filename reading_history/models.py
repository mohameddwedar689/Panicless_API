# Imports standard libraries
#...

# Imports core Django libraries
import django
from django.db import models

# Imports third-party libraries
#...

# Imports from your apps
from account.models import User

class Reading(models.Model):
    """models for reading app """
    user           = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='reading', verbose_name='username')
    heart_rate     = models.PositiveIntegerField()
    breathing_rate = models.PositiveIntegerField()
    trembling_rate = models.PositiveIntegerField()
    message        = models.CharField(max_length=130)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Retrive string representation of our reading"""
        return str(self.id)

    class Meta:
        db_table = 'Readings'