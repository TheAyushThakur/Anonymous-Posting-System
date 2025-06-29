from django import forms
from .models import AnonymousPost, Comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = AnonymousPost
        fields = ['mood', 'message']
        widgets = {
            'mood': forms.Select(attrs= {'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': "What's on your mind?",
            }),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        odel = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...'}),
        }