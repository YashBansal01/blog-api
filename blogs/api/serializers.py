from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
from api.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'owner']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    @staticmethod
    def create(validated_data):
        user = User.objects.create_user(validated_data['username'], 
        email= validated_data['email'],
        password= validated_data['password'], 
        first_name=validated_data['first_name'], 
        last_name=validated_data['last_name'])
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user', 'dob', 'address', 'phone_number'
        )