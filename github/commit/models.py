from django.db import models

class Commit(models.Model):
    sha = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    size = models.IntegerField()
    commitedDate = models.DateTimeField(auto_now_add=True)
