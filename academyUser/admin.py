from django.contrib import admin
from . import models

class AccountAdmin(admin.ModelAdmin):
        list_display = ['username', 'email', 'role']

class ModuleAdmin(admin.ModelAdmin):
        list_display = ['title']



admin.site.register(models.Account, AccountAdmin)

admin.site.register(models.Contact)

admin.site.register(models.Course)

admin.site.register(models.Module, ModuleAdmin)


