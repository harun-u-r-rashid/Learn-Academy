
from django.db import models

from academyUser.models import Account


class Student(models.Model):
        account = models.OneToOneField(Account, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='student/', blank=True, null=True)
        def __str__(self):
                return f"{self.account.username}"
        


        
