from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserProfile, Post
from .serializers import UserProfileSerializer, PostSerializer
from rest_framework.exceptions import PermissionDenied
# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def user_profile_view(request):
#     """Retrieve or update the user profile."""
#     profile = get_object_or_404(UserProfile, user=request.user)
#     if request.method == 'GET':
#         serializer = UserProfileSerializer(profile)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserProfileSerializer(profile, data=request.data,
#         partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_create_view(request):
    """List all posts or create a new post."""
    if request.method == 'GET':
        # Get all post from the database
        posts = Post.objects.all()
        # Pass our input into the serializers
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data,
        status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)