from rest_framework import serializers
from .models import UserProfile, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio')
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at',
        'updated_at')

# class PostSerializerResponse(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#     class Meta:
#         model = Post
#         fields = ('id','title', 'content', 'author', 'created_at',
#         'updated_at')
