from django.db import models
from django import forms
from django.core.validators import RegexValidator
# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.core.validators import RegexValidator

class UserProxy(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password = forms.CharField(min_length=10, required=True, validators=[RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#])(?=.{10,})', message="Enter a valid password")],
    help_text='Required.', widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password','email')
