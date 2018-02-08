# rest_api/views.py

from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ServantSerializer
from .models import Servant
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class CreateView(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer

    def perform_summoning(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer
