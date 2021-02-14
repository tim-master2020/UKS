from django.db import models
from task.models import Task
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='commentFiles/',blank=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
