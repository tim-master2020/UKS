from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# Create your models here.
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