from django.db import models

# Create your models here.

class Wiki(models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.content 