# jwt_auth/models.py 

from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    name = models.TextField(max_length = 200, blank = False)
    student_id = models.PositiveIntegerField(max_length= 8, blank = False)
    library_no = models.PositiveIntegerField(blank = False)
    email = models.EmailField(unique = True)
