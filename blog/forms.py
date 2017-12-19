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
        fields = ('text',)
        widgets = {
                'text': forms.TextInput(attrs={'Plcaeholder': 'comment'}),
                }
