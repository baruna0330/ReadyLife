from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #CHOICES = (('public', 'public'),('private', 'private'),)
    #category = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Post
        fields = '__all__'
        #field = ['title', 'body', 'category',]