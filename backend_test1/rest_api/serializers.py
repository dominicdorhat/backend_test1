# rest_api/serializers.py 

from rest_framework import serializers
from .models import Servant

class ServantSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Servant
        fields = ('id', 'name', 'master', 'servant_class', 'noble_phantasm')