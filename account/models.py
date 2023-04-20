# Imports standard libraries
#...

# Imports core Django libraries
from django.db import models
from django.contrib.auth.models import AbstractUser

# Imports third-party libraries
#...

# Imports from your apps
from account import manager


class Account(AbstractUser):
    username     = models.CharField(max_length=255,unique=True)
    first_name   = models.CharField(max_length=255,blank=True,null=True)
    last_name    = models.CharField(max_length=255,blank=True,null=True)
    phone_number = models.CharField(max_length=11,unique=True)
    email        = models.EmailField(max_length=255,unique=True)
    photo        = models.ImageField(blank=True,null=True,upload_to='profile/')
    is_suspended = models.BooleanField(default=False)
    is_blocked   = models.BooleanField(default=False)

    # Assign Manager to Model
    objects = manager.AccountManager()
    # Put username ==> phone_number
    USERNAME_FIELD = 'phone_number'
    # Choise Required fieldes
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    def __str__(self):
        """Retrive string representation of our user"""
        return self.phone_number


    class Meta:
        db_table ='Account'
