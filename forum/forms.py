from django import forms
from .models import AnonymousPost

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
