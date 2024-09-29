from django.urls import path
from .views import UserRegistrationView, Userlogin

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'userregister'),
    path('login/', Userlogin.as_view(), name= 'userlogin'),
]