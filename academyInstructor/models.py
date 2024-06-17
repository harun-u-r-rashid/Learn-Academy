from django.db import models

from academyUser.models import Account


class Instructor(models.Model):
        account = models.OneToOneField(Account, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='instructor/', blank=True, null=True)
        def __str__(self):
                return f"{self.account.username}"
        

    

        
