# jwt_auth/models.py 

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager 

# class CustomUserManager(UserManager):
#     pass

class User(AbstractUser):
    name = models.TextField(max_length = 200, blank = False)
    student_id = models.IntegerField(null = True)
    library_no = models.IntegerField(null = True)
    email = models.EmailField(unique = True)

    # Use UserManager to get the standard methods
    objects = UserManager()