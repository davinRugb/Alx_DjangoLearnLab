from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    bio = models.TextField
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followering')

    def __str__(self):
        return self.username

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username