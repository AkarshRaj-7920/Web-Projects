from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'location', 'description']

        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'input-field',
                'placeholder': 'Title',
            }),

            'image': forms.FileInput(),

            'location': forms.TextInput(attrs = {
                'class': 'input-field',
                'placeholder': 'Image Location',
            }),

            'description': forms.Textarea(attrs = {
                'class': "desc-field",
                'rows': "3", 
                'placeholder': "Description", 
            }),
        }

