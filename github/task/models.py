from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from label.models import Label
from milestone.models import Milestone
from project.models import Project
from repository.models import Repository

class TaskStatus(Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    TEST = "TEST"
    DONE = "DONE"

class TaskState(Enum):
    OPENED = "OPENED"
    CLOSED = "CLOSED"

class TaskPriorty(Enum):
    LOW = "LOW"
    MEDUIM = "MEDUIM"
    HIGH = "HIGH"

class TaskType(Enum):
    BUG_FIX = "BUG_FIX"
    FEATURE = "FEATURE"

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300,blank=True)
    openingDate = models.DateTimeField(auto_now_add=True)
    taskStatus = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskStatus], default="TO_DO")
    taskState = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskState],default="OPENED")
    taskPriorty = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskPriorty],default="LOW")
    taskType = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskType],default="FEATURE")
    labels = models.ManyToManyField(Label)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='author')
    asignees = models.ManyToManyField(to=User, blank=True)
    milestone = models.OneToOneField(Milestone,on_delete=models.CASCADE)
    repo = models.ForeignKey(to=Repository,on_delete=models.CASCADE,related_name='repo')
    project = models.ManyToManyField(to=Project,null=True)



