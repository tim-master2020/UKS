from django.db import models 
from user.models import UserModel

class Commit(models.Model):
    sha = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    size = models.IntegerField()
    commitedDate = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(UserModel, verbose_name='user', on_delete=models.CASCADE)
