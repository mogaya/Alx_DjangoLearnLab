from django.shortcuts import render
# from rest_framework.views import ApiView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

CustomUser = get_user_model()

# Create your views here.
class RegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Follow Management Views
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            if request.user == target_user:
                return Response({"detail": "You can not follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            if request.user.is_following(target_user):
                return Response({"detail": "You already follow this user"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.follow(target_user)
            return Response({"detail": "Followed Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"detail": "CustomUser not found"}, status=status.HTTP_403_FORBIDDEN)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            if not request.user.is_following(target_user):
                return Response({"detail": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.unfollow(target_user)
            return Response({"detail": "Unfollowed Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"detail": "CustomUser not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # To ensure the user is logged in

    def get(self, request, *args, **kwargs):
        # You can list all users or filter based on your needs
        users = CustomUser.objects.all()  # Get all users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)