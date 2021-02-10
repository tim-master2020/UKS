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
    closingDate = models.DateTimeField(null=True,blank=True)
    taskStatus = models.CharField(max_length=50,choices = [(tag.value, tag.name) for tag in TaskStatus], default=TaskStatus.TO_DO.name,blank=True)
    taskState = models.CharField(max_length=50,choices = [(tag.value, tag.name) for tag in TaskState],default=TaskState.OPENED.name,blank=True)
    taskPriorty = models.CharField(max_length=50,choices = [(tag.value, tag.name) for tag in TaskPriorty],default=TaskPriorty.LOW.name,blank=True)
    taskType = models.CharField(max_length=50,choices = [(tag.value, tag.name) for tag in TaskType],default=TaskType.FEATURE.name,blank=True)
    labels = models.ManyToManyField(Label,blank=True)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='author')
    asignees = models.ManyToManyField(to=User, blank=True)
    milestone = models.ManyToManyField(to=Milestone,blank=True)
    repo = models.ForeignKey(to=Repository,on_delete=models.CASCADE,related_name='repo')
    project = models.ManyToManyField(to=Project,blank=True)

    def __str__(self):
        return self.title 

