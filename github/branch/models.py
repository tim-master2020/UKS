from django.db import models
from django.utils.translation import gettext_lazy as _
from repository.models import Repository


class Branch(models.Model):
    name = models.CharField(max_length=50)
    repository = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return self.name