from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='User Name', max_length=30,
                               help_text="user name couldn't have spaces")
    email = forms.EmailField(label='Email')
    # first_name = forms.CharField(label='الاسم الأول')
    # last_name = forms.CharField(label='الاسم الأخير')

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
        (attrs={'id' : 'passwordField'}) ,min_length=8,
    )
    # password2 = forms.CharField(
    #     label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1',)

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password1'] != cd['password2']:
    #         raise forms.ValidationError('كلمة المرور غير متطابقة')
    #     return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('thios user name already exist')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='User Name')
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    # first_name = forms.CharField( )
    # last_name = forms.CharField( )
    user_name    = forms.CharField( )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)