from django.db import models
from wiki.models import Wiki
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Repository(models.Model):
    name = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now_add=True)
    wiki = models.OneToOneField(Wiki, on_delete=models.CASCADE)
    user=models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name