from django.db import models

# Create your models here.

class Wiki(models.Model):
    content = models.CharField(max_length=500)