from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import InstructorSerializer #, CourseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class InstructorView(viewsets.ModelViewSet):
        queryset = models.Instructor.objects.all()
        serializer_class = InstructorSerializer
        permission_classes = [IsAdminUser]



    



