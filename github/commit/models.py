from django.db import models 
from django.contrib.auth.models import User
from branch.models import Branch

class Commit(models.Model):
    sha = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    commitedDate = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    branch = models.ForeignKey(to=Branch, on_delete=models.DO_NOTHING,null=True)
