# rest_api/views.py

from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ServantSerializer
from .models import Servant

class CreateView(generics.ListCreateAPIView):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_summoning(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )
