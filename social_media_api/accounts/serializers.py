from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
 
User = get_user_model

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture', 'followers', 'email', 'username','password']

class UserRegistrationserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ['email', 'profile_picture', 'password', 'username']
        extra_kwards = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        created_user = get_user_model().objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            username = validated_data['username'],
        )

        return created_user
    
        Token.objects.create(user=user)
        
        return user

class Userloginserializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()