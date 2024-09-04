from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line
]



