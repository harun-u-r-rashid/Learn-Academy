from django.db import models

from academyUser.models import Account


class Instructor(models.Model):
        account = models.OneToOneField(Account, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='instructor/', blank=True, null=True)
        def __str__(self):
                return f"{self.account.username}"
        

# class Course(models.Model):
#         instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
#         title = models.CharField(max_length=100)
#         description = models.TextField(max_length=200)
#         price = models.IntegerField()
#         image = models.ImageField(upload_to='course/', blank=True, null=True)
        
#         created_at = models.DateTimeField(auto_now_add=True)

#         def __str__(self):
#                 return f"{self.title}"
        
        

        
