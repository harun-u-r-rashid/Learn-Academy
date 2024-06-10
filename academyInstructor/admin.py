from django.contrib import admin
from . import models

class InstructorAdmin(admin.ModelAdmin):
        list_display = ['account', 'email']  

        def email(self,obj):
            return obj.account.email
        

class CourseAdmin(admin.ModelAdmin):
      list_display = ['instructor', 'title']
        
admin.site.register(models.Instructor, InstructorAdmin)

admin.site.register(models.Course, CourseAdmin)

