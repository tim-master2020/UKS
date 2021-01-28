from django.db import models
from project.models import Project

# Create your models here.

class Milestone(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    start = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)