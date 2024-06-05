from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        

class Auth(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
    def save(self, **kwargs):
        new_user = User.objects.create_user(
            username=self.validated_data['username'],
            email = self.validated_data['email'],
            password = self.validated_data['password'],
        )
        
        new_user.save()
        
        Token.objects.create(user=new_user)
        
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)  # Create a token for the new user
    #     return user