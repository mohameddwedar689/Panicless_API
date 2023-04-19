from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, trustNumber, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            trustNumber=trustNumber,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstName, lastName, trustNumber, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            trustNumber=trustNumber,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """ models for account app """
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    trustNumber = models.CharField(max_length=255)
    email       = models.EmailField(verbose_name="email address",max_length=255,unique=True,error_messages={"unique": "A user with this email already exists."},validators=[validators.EmailValidator(message="Not valid Email")],)
    image       = models.ImageField(upload_to="user/images",blank=True,null=True,verbose_name=("Image"),)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_update = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("trustNumber", "firstName", "lastName")
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
