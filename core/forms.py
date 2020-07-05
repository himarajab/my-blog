from django import forms

from .models import Data


class DataForm(forms.ModelForm):
    
    # def clean_title(self):
    #     result = self.cleaned_data['title']
    #     data = result + str(self.cleaned_data['pk'])
    #     print(data)
    #     return data

    class Meta:
        model = Data
        fields='title','body'
        # fields='__all__'

        # key-value pair of fields and the desired style
        widgets={
            # any attribute to input field pass it as dictionary
            # 'url':forms.TextInput(attrs={
            #     'class':'form-control',
            # }),
            
            'title':forms.TextInput(attrs={
                'class':'form-control',
            }),

            'body': forms.TextInput(attrs={
                'class': 'form-control',

            }),
        }

