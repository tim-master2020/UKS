from django.db import models
from task.models import Task

class Comment(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True, blank=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE,null=True)
