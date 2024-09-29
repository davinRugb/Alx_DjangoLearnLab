from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from django.urls import path
from .views import FeedView
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:post_id>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]