from django.contrib import admin
from . import models

class StudentAdmin(admin.ModelAdmin):
        list_display = ['account', 'email']  

        def email(self,obj):
            return obj.account.email
        
admin.site.register(models.Student, StudentAdmin)