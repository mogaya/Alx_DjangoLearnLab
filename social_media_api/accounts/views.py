from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Follow Management Views
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
            if request.user == target_user:
                return Response({"detail": "You can not follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            if request.user.is_following(target_user):
                return Response({"detail": "You already follow this user"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.follow(target_user)
            return Response({"detail": "Followed Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_403_FORBIDDEN)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
            if not request.user.is_following(target_user):
                return Response({"detail": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.unfollow(target_user)
            return Response({"detail": "Unfollowed Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)