from django import forms
import re
from .models import Data
import json
from django.utils.translation import ugettext_lazy as _


class DataForm(forms.ModelForm):
    body = forms.CharField(max_length=200, required=False)

    def clean_body(self):
        # to remove wiered empty strings in the result
        # the () in the pattern to keep the sepreators cause i'll need it when joining

        data_dict = []

        test_str = self.cleaned_data['body']
        
        data = re.split('([?.;\n])', test_str.strip())
        for i,elem in enumerate(data):
            data_dict.append([i ,elem,1])

        # import ipdb ; ipdb.set_trace()
       
        data =re.sub("[\[\]\']", "", str(data))
        
        # data = []

        # for elem in data_list:
        #     data.append(elem+'hello')


        # print(f'\n {data},{type(data)}\n')

        return data

    class Meta:
        model = Data
        fields='title','body'
        # fields='__all__'
    # def clean(self):
    #     for field, value in self.cleaned_data.items():
    #         self.cleaned_data['body'] = value.lower()


        # key-value pair of fields and the desired style
        widgets={
            # any attribute to input field pass it as dictionary
            # 'url':forms.TextInput(attrs={
            #     'class':'form-control',
            # }),
            
            'title':forms.TextInput(attrs={
                'class':'form-control',
            }),
        }


class UpdateForm(forms.ModelForm):
    body = forms.CharField(max_length=200, required=False)

    def clean_body(self):
        data = str(self.cleaned_data['body'])
        # print(f'\n {data}clean_update_body \n')
        return data

    class Meta:
        model = Data
        fields='title','body'



        # key-value pair of fields and the desired style
        widgets={
            # any attribute to input field pass it as dictionary
            # 'url':forms.TextInput(attrs={
            #     'class':'form-control',
            # }),
            
            'title':forms.TextInput(attrs={
                'class':'form-control',
            }),
        }

