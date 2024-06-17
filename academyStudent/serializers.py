from rest_framework import serializers
from . import models
from academyUser.models import Course

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.Student
                fields = '__all__'

