from django.urls import path
from .views import UserRegistrationView, Userlogin
from django.urls import path
from .views import FollowUserView, UnfollowUserView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'userregister'),
    path('login/', Userlogin.as_view(), name= 'userlogin'),
]


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow'})),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow'})),
]


urlpatterns = [
    path('users/<int:pk>/follow/', FollowUserView.as_view(), name='follow_user'),
    path('users/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow_user'),
]

from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    # Other URL patterns can be added here

    # Route for following a user
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),

    # Route for unfollowing a user
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]