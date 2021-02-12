from django import forms 
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password = forms.CharField(min_length=10, required=True, validators=[RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#])(?=.{10,})', message="Enter a valid password")],
                               help_text='Required.', widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password','email')

class UserUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
