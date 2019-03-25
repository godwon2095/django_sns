from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'user']
        labels = {
            'title': "제목",
            'image': "이미지",
            'content': "내용",
        }
        widgets = {
            'user': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'body']
        labels = {
            'body': "내용",
        }
        widgets = {
            'user': forms.HiddenInput(),
            'post': forms.HiddenInput(),
        }