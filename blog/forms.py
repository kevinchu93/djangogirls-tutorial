from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
                'text': forms.TextInput(attrs={'Placeholder': 'teriyaki chicken'}),
                'title': forms.TextInput(attrs={'Placeholder': 'titl'})
                }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
                'author': forms.TextInput(attrs={'Placeholder': 'author'}),
                'text': forms.TextInput(attrs={'Placeholder': 'comment'}),
                }
