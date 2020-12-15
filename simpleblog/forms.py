
from  django import forms
from .models import *
from mptt.forms import TreeNodeChoiceField
# model form allow to create form fields to our model
# if i want to fitch values from another model
# first in the db
choices=Category.objects.all().values_list('name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','author','category','content')
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
            'content': forms.TextInput(attrs={
                'class': 'form-control'
            }),
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
        fields= ('title','content')
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
            'content': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False 
        self.fields['parent'].label = ''
        # remove the elment from the view
        self.fields['parent'].widget.attrs.update({'class':'d-none'})
    class Meta:
        model = Comment
        fields = ( 'parent', 'content','post')
        widgets = {

            'content': forms.Textarea(attrs={'class': 'ml-3 mb-3 form-control border-0 comment-add rounded-0','rows':'1','placeholder':'add a public comment'}),
        }
    def save(self, *args, **kwargs):
       Comment.objects.rebuild()
       super(NewCommentForm, self).save(*args, **kwargs) # Call the real save() method


class PostSearchForm(forms.Form):
    q=forms.CharField()
    # category = forms.ModelChoiceField(queryset = Category.objects.all().order_by('name'))   

    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        # self.fields['category'].required = False
        
        # self.fields['category'].label = 'Category'
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update({'class':'form-control menudd'})
        self.fields['q'].widget.attrs.update({'data-toggle':'dropdown'})
    
