from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.Account
                fields = '__all__'




class UserRegSerializer(serializers.ModelSerializer):
        confirm_password = serializers.CharField(required = True)
        class Meta:
                model = models.Account
                fields = ['username', 'first_name', 'last_name', 'role', 'email', 'password', 'confirm_password']

        def save(self):
                username = self.validated_data['username']
                first_name = self.validated_data['first_name']
                last_name = self.validated_data['last_name']
                email = self.validated_data['email']
                role = self.validated_data['role']
                password = self.validated_data['password']
                confirm_password = self.validated_data['confirm_password']


                if password!=confirm_password:
                        raise serializers.ValidationError({'error':"Password doesn't match"})
                
               
                if models.Account.objects.filter(username = username).exists():
                        raise serializers.ValidationError({'error': "Username already exists"})
                
                if models.Account.objects.filter(email=email).exists():
                        raise serializers.ValidationError({'error': "Email already exists"})
                

                account = models.Account(
                        username=username, 
                        email=email, 
                        first_name=first_name,
                        last_name=last_name,
                        role = role
                        )
                account.set_password(password)
                account.is_active = False
                account.save()

                return account
        



class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField(required = True)
        password = serializers.CharField(required = True)

                
# reset password


class PasswordResetSerializer(serializers.Serializer):
        email = serializers.EmailField(required = True)


    
class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid': ('Password must be at least 8 characters long with at least one capital letter and symbol')}
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data




# contact serializer

class ContactSerializer(serializers.ModelSerializer):
       class Meta:
              model = models.Contact
              fields = '__all__'