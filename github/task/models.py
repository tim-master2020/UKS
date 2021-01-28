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

