from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import InstructorSerializer #, CourseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class InstructorView(viewsets.ModelViewSet):
        queryset = models.Instructor.objects.all()
        serializer_class = InstructorSerializer



# class CourseView(viewsets.ModelViewSet):
#         queryset = models.Course.objects.all()
#         serializer_class = CourseSerializer


# class CourseCreateView(generics.CreateAPIView):
#         serializer_class = CourseSerializer
#         # permission_classes = [IsAuthenticated]

#         def perform_create(self, serializer):
#                 new_course = serializer.save()
#                 new_course.save()


# class CourseUpdateView(generics.UpdateAPIView):
#         queryset = models.Course.objects.all()
#         serializer_class = CourseSerializer
#         # permission_classes

#         def perform_update(self, serializer):
#                 update_course = serializer.save()


# class CourseDestroyView(generics.DestroyAPIView):
#         queryset  = models.Course.objects.all()
        



