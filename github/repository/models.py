from django.db import models
from django.utils.translation import gettext_lazy as _


class Repository(models.Model):
    name = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name