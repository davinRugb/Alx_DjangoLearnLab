from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile_view
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostListView, PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),  # Profile view to be implemented
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_pk>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('posts/<int:post_pk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
]

tags/<slug:tag_slug>/", "PostByTagListView.as_view()