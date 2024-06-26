from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .constants import ROLES

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        if not username:
            raise ValueError("User must have an username")
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username, 
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user
    
    
    
class Account(AbstractBaseUser):
    username = models.CharField(max_length = 30, unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30, unique = True)
    phone_number = models.CharField(max_length = 30)
    role = models.CharField(max_length=30, choices=ROLES, null=True, blank=True)

    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superadmin        = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']
    
   
    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



# Passowrd reset


class PasswordReset(models.Model):
        email = models.EmailField()
        createDate = models.DateTimeField(auto_now_add = True)



# Contact

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query = models.TextField(max_length=300)


    def __str__(self):
        return f"{self.name}"
    
    

# Course
class Course(models.Model):
        account = models.ForeignKey(Account, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        description = models.TextField(max_length=200)
        price = models.IntegerField()
        image = models.ImageField(upload_to='course/', blank=True, null=True)
        
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return f"{self.title}"
    
# Module 

class Module(models.Model):
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     url = models.URLField()

     def __str__(self):
          return f"{self.title}"
     

     