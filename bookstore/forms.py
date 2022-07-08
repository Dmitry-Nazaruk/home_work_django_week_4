from django import forms
from .models import Authors, Books


class PostForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'author_id']
