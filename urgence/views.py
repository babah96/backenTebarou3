from django.shortcuts import render
from.models import*
from rest_framework import status
from rest_framework import generics,viewsets
from .serialisers import UrgenceSerializer
from django.http import JsonResponse

# generic views
# class UrgenceList(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Urgence.objects.all()
#     serializer_class=UrgenceSerializer

# viewsets
class UrgenceViewset(viewsets.ModelViewSet):
     queryset=Urgence.objects.all()
     serializer_class=UrgenceSerializer