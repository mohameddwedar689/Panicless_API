# Imports standard libraries
#...

# Imports core Django libraries
from django.contrib.auth.models import BaseUserManager

# Imports third-party libraries
#...

# Imports from your apps
#...

# extends base user manager and override create user method & create super user
class AccountManager(BaseUserManager):
    """
    account model manager where  is the unique identifiers
    for authentication instead of username use phone_number_number as unique field.
    """
    def create_user(self, username, first_name=None, last_name=None, phone_number=None, email=None, password=None, **extra_fields):
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone_number, email, password, **extra_fields):
        """
        Create and save a account for super user with the given phone_number_number and password in db.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username, first_name, last_name, phone_number, email, password, **extra_fields)
