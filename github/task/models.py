from django.db import models
from enum import Enum
from label.models import Label

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
    description = models.CharField(max_length=300)
    openingDate = models.DateTimeField(auto_now_add=True)
    closingDate = models.DateTimeField(null=True)
    taskStatus = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskStatus], default="TO_DO")
    taskState = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskState],default="OPENED")
    taskPriorty = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskPriorty],default="LOW")
    taskType = models.CharField(max_length=50,choices = [(tag, tag.value) for tag in TaskType],default="FEATURE")
    label = models.ManyToManyField(Label)




