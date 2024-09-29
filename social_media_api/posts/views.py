from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import filters
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# Base class to handle post actions
class BasePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model_class = Post

    def get_post(self, pk):
        # Fetch the post using get_object_or_404 from the model class
        return get_object_or_404(self.model_class, pk=pk)


class LikePostView(BasePostView):
    def post(self, request, pk):
        post = self.get_post(pk)
        # Prevent duplicate likes by checking if the like already exists
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"message": "You already liked this post"}, status=400)
        
        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_ct=ContentType.objects.get_for_model(Post),
            target_id=post.id
        )
        
        return Response({"message": "Post liked"}, status=200)


class UnlikePostView(BasePostView):
    def post(self, request, pk):
        post = self.get_post(pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=200)
        else:
            return Response({"message": "You haven't liked this post yet"}, status=400)

from django.shortcuts import get_object_or_404  # Correct import
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Example View to handle getting a Post object
class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()

    def get(self, request, pk):
        # Correctly use get_object_or_404 to retrieve the post
        post = get_object_or_404(Post, pk=pk)
        return Response({"post": post.title, "content": post.content}, status=200)