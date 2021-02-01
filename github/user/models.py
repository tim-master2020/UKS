from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProxy(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'


