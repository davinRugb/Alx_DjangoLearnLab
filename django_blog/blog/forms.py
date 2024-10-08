from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from .models import Post, Tag
from taggit.forms import TagField 
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Include the 'content' field from the Comment model




class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# blog/forms.py

 # Import TagField from django-taggit

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Use TagField for tag management

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


TagWidget()", "widgets