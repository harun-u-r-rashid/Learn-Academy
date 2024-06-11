from rest_framework import serializers
from . import models


class InstructorSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.Instructor
                fields = '__all__'


# class CourseSerializer(serializers.ModelSerializer):
#         def countCourse(self, instance):
#                 total = models.Course.objects.filter(course=instance).count()
#                 return total
        
#         class Meta:
#                 model = models.Course
#                 fields = '__all__'

        