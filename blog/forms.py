from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
                'text': forms.TextInput(attrs={'Placeholder': 'teriyaki chicken'}),
                'title': forms.TextInput(attrs={'Placeholder': 'titl'})
                }
