from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile_view
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),  # Profile view to be implemented
]
