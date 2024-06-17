from django.shortcuts import render
from rest_framework import viewsets, status
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
#  password reset
from rest_framework import generics
from django.utils.encoding import force_str


class UserViewSet(viewsets.ModelViewSet):
        queryset = models.Account.objects.all()
        serializer_class = serializers.UserSerializer
        permission_classes = [AllowAny]

# Contact ja ache sob view korabe

class ContactView(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer 
    permission_classes = [AllowAny]




class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserRegSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # https://learn-academy.onrender.com/
            confirm_link = f"https://learn-academy.onrender.com/user/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)
  


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = models.Account._default_manager.get(pk=uid)
    except(models.Account.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
       
        # https://shikboacademy.netlify.app/
        return redirect('https://shikboacademy.netlify.app/login')
    else:
        return redirect('register')
    


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)



class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')



# reset password

class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        user = models.Account.objects.filter(email__iexact=email).first()

        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # https://learn-academy.onrender.com/
            confirm_link = f"https://learn-academy.onrender.com/user/password-reset/{uid}/{token}"

            email_subject = "Confirm Your Email"
            email_body = render_to_string('resetEmail.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        else:
             return Response("User not found")
    

class ResetPassword(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = models.Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, models.Account.DoesNotExist):
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)
        

        

        if not default_token_generator.check_token(user, token):
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password']
        
        if new_password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        
        return Response({'success': 'Password updated successfully'}, status=status.HTTP_200_OK)



# Contact add korbe
class ContactAddView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"Failed to send your query!"}, status=status.HTTP_400_BAD_REQUEST)


# Course view

class CourseView(viewsets.ModelViewSet):
        queryset = models.Course.objects.all()
        serializer_class = serializers.CourseSerializer
        permission_classes = [AllowAny]


class CourseCreateView(generics.CreateAPIView):
        serializer_class = serializers.CourseSerializer
        permission_classes = [IsAdminUser]

        def perform_create(self, serializer):
                new_course = serializer.save()
                new_course.save()


class CourseUpdateView(generics.UpdateAPIView):
        queryset = models.Course.objects.all()
        serializer_class = serializers.CourseSerializer
        permission_classes = [IsAdminUser]

        def perform_update(self, serializer):
                update_course = serializer.save()


class CourseDestroyView(generics.DestroyAPIView):
        queryset  = models.Course.objects.all()
        


# Module Views

class ModuleView(viewsets.ModelViewSet):
     queryset = models.Module.objects.all()
     serializer_class = serializers.ModuleSerializer
     permission_classes = [AllowAny]

    
class ModuleCreateView(generics.CreateAPIView):
     serializer_class = serializers.ModuleSerializer
    #  permission_classes = [IsAdminUser]
     def perform_create(self, serializer):
          create_module = serializer.save()
          create_module.save()

    
class ModuleUpdateView(generics.UpdateAPIView):
     queryset = models.Module.objects.all()
     serializer_class = serializers.ModuleSerializer
    #  permission_classes = [IsAdminUser]

     def perform_update(self, serializer):
          update_module = serializer.save()


class ModuleDestroyView(generics.DestroyAPIView):
     queryset = models.Module.objects.all()


     