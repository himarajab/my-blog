from  django import forms
from .models import *

# model form allow to create form fields to our model
# if i want to fitch values from another model
# first in the db
choices=Category.objects.all().values_list('name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','title_tag','author','category')
        # fields='__all__'
        # key-value pair of fields and the desired style
        widgets={
            # any attribute to input field pass it as dictionary
            'title':forms.TextInput(attrs={
                'class':'form-control',
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'value' : '',
                'id':'forJs',
                'type':'hidden'
            }),
            # 'author': forms.Select(attrs={
            #     'class': 'form-control'
            # }),
            # if want to put choices put it before attrs
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'value' : '',
                'placeholder': choices
            }),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','title_tag','body')
        # fields='__all__'
        # key-value pair of fields and the desired style
        widgets={
            # any attribute to input field pass it as dictionary
            'title':forms.TextInput(attrs={
                'class':'form-control','placeholder':'title placeholder'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        # # fields='__all__'
        # # key-value pair of fields and the desired style
        # widgets = {
        #     # any attribute to input field pass it as dictionary
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'email': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'body': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        # }