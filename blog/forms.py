from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget)
    # publish = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')