from django.db import models
from django import forms
from django.core.validators import RegexValidator
# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone


class UserProxy(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'


class UserModel(models.Model):
    user = models.OneToOneField(UserProxy, related_name='profile', on_delete=models.PROTECT)
    username=models.CharField('username', max_length=500)
    name = models.CharField('name', max_length=500)
    first_name=models.CharField('first name', max_length=500)
    last_name=models.CharField('last name', max_length=500)
    email = models.EmailField('email', max_length=500)
    password = models.EmailField('password', max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'GitHub user'
        verbose_name_plural = 'GitHub users'

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password = forms.CharField(min_length=10, required=True, validators=[RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#])(?=.{10,})', message="Enter a valid password")],
    help_text='Required.', widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password','email')
