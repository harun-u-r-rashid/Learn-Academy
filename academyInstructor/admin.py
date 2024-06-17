from django.contrib import admin
from . import models

class InstructorAdmin(admin.ModelAdmin):
        list_display = ['account', 'email']  

        def email(self,obj):
            return obj.account.email
        

     
admin.site.register(models.Instructor, InstructorAdmin)
