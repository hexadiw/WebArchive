from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Archive
from .serializers import ArchiveSerializer

class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer