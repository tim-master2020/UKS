from django.db import models
from wiki.models import Wiki

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    wiki = models.OneToOneField(Wiki, on_delete=models.CASCADE)
