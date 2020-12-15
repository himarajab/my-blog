from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from .models import Profile
from django.core.exceptions import ValidationError

class pwdChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password" , widget=forms.PasswordInput(
        attrs={'class':'form-conrol mb-3','placeholder':'Old Password','id':'form-oldpass'}
    ))

    new_password1 = forms.CharField(label="New Password" , widget=forms.PasswordInput(
        attrs={'class':'form-conrol mb-3','placeholder':'New Password','id':'form-newpass'}
    ))

    new_password2 = forms.CharField(label="Repeat Password" , widget=forms.PasswordInput(
        attrs={'class':'form-conrol mb-3','placeholder':'new Password','id':'form-new-pass2'}
    ))


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254,widget=forms.TextInput(
        attrs={'class':'form-control mb-3' , 'placeholder':'email','id':'form-email'}
    ))
    # this solution include security risks cause it's allow attacker to know what emails are exist in the db ; but it's a good initial solution 
    def clean_email(self):
        email = self.cleaned_data['email']

        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError(
            "unfortuanately  we can't find that email"
        )
        return email
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='User Name', max_length=30,
                               help_text="Required")
    email = forms.EmailField(label='Email',help_text="Required",error_messages={'required':'Sorry , you will need an email'})
    # first_name = forms.CharField(label='الاسم الأول')
    # last_name = forms.CharField(label='الاسم الأخير')

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
        (attrs={'id' : 'passwordField'}) ,min_length=8,
    )
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1',)

    
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError('Passwords do not Match')
        return cd['password2']

    
    
    def clean_username(self):
        user_name = self.cleaned_data['username'].lower()
        r= User.objects.filter(username=user_name)
        if r.count():
            raise ValidationError('this user name already exist')
        return user_name
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r= User.objects.filter(email=email)
        if r.exists():
            raise ValidationError('this Email already exist')
        return email

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'form-control mb-3','placeholder':'Username'
        })

        self.fields['email'].widget.attrs.update({
            'class':'form-control mb-3','placeholder':'Email','name':'email'
        })

        self.fields['password1'].widget.attrs.update({
            'class':'form-control','placeholder':'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-control ','placeholder':'Repeat Password'
        })







class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'UserName','id':'login-username'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Password',
            'id':'login-pwd'}
        ))
     



# class LoginForm(forms.ModelForm):
#     username = forms.CharField(label='User Name')
#     password = forms.CharField(
#         label='Password', widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ('username', 'password')




class UserUpdateForm(forms.ModelForm):
    # first_name = forms.CharField( )
    # last_name = forms.CharField( )
    # user_name    = forms.CharField( )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)