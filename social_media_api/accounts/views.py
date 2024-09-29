from rest_framework import generics,permissions,status
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken import RefreshToken
from rest_framework.authtoken.views import TokenObtainPairView
from .serializers import UserRegistrationserializer,UserSerializers, Userloginserializers
from rest_framework.authtoken.models import Token              
from rest_framework.authtoken.views import ObtainAuthToken


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # if user.objects.filter(email=request.data['email']).exists():
        #     return Response({
        #     "message":"This Email Already Exists",
        # },status=status.HTTP_400_CREATED)

        # if user.objects.filter(username=request.data['username']).exists():
        #     return Response({
        #     "message":"This Email Already Exists",
        # },status=status.HTTP_400_CREATED)

        serializer.is_valid(raise_exception=True)  # Validate data
        user = serializer.save()  # Create the user
        user_data = UserRegistrationserializer(user).data
        return Response({
            "message":"User created successfully",
            "user":user_data,
        },status=status.HTTP_201_CREATED)


class Userlogin(ObtainAuthToken):
    serializer_class = Userloginserializers

    def post(self, request, *args, **kwargs):
        Serializer = self.serializer_class(data = request.data)
        Serializer.is_valid(raise_exception=True)  # Validate data
        email = Serializer.validated_data['email']
        password = Serializer.validated_data['password']
        
        user=User.objects.get(email=email)
        
        if user.check_password(password):
            token=RefreshToken.for_user(user)

            return Response({
                "message":'User Login sucessfull',
                'user':UserSerializers(user).data,
                "accessToken":str(token)
                
            })
        else:
            return Response({
                "message":'Invalid Email or Password',
            },status=status.HTTP_400_BAD_REQUEST)



