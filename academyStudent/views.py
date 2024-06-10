from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import StudentSerializer

class StudentView(viewsets.ModelViewSet):
        queryset = models.Student.objects.all()
        serializer_class = StudentSerializer
        