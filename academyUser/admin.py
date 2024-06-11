from django.contrib import admin
from . import models

class AccountAdmin(admin.ModelAdmin):
        list_display = ['username', 'email', 'role']

admin.site.register(models.Account, AccountAdmin)


admin.site.register(models.Contact)

admin.site.register(models.Course)
