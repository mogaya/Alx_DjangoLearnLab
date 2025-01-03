# from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed Functionality View
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use generics.get_object_or_404 to get the post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Ensure a user cannot like their own post
        if request.user == post.author:
            return Response({"detail": "You cannot like your own post"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use Like.objects.get_or_create to either create a new like or get the existing one
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        
        # create notification
        notification = Notification.objects.create(
            recipient = post.user,
            actor = request.user,
            verb = "liked your post",
            target = post,
        )

        return Response({"detail": "Post liked", "notification": notification.id}, status=status.HTTP_200_OK)
        
        # return Response({"detail": "Post liked successfully"}, status=status.HTTP_200_OK)
    

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use generics.get_object_or_404 to get the post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Ensure a user cannot unlike their own post
        if request.user == post.author:
            return Response({"detail": "You cannot unlike your own post"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Try to get the Like object for the given post and user, and delete it
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)

    
# #  views to like and unlike posts.
# class LikePostView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk):
#         post = generics.get_object_or_404(Post, pk=pk)
#         if Like.objects.filter(user=request.user, post=post).exists():
#             return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        
#         like = Like.objects.create(user=request.user, post=post)

#         # create notification
#         notification = Notification.objects.create(
#             recipient = post.user,
#             actor = request.user,
#             verb = "liked your post",
#             target = post,
#         )

#         return Response({"detail": "Post liked", "notification": notification.id}, status=status.HTTP_200_OK)
    
# class UnlikePostView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         like = Like.objects.filter(user=request.user, post=post).first()
#         if not like:
#             return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        
#         like.delete()
#         return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)