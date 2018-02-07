# rest_api/models.py

from django.db import models
from jwt_auth.models import User

class Servant(models.Model):

    name = models.CharField(max_length = 255, blank = False)
    master = models.ForeignKey('jwt_auth.User', on_delete = models.CASCADE)
    servant_class = models.CharField(max_length = 255)
    noble_phantasm = models.CharField(max_length = 255)


    def __str__(self):
        return "{}".format(self.name)

    