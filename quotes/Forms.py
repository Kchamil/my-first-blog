from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'text', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Post'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Page'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Post'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Page'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Post'}),
        }