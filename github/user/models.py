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


