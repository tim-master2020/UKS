from django.db import models
from django.core.validators import RegexValidator
from repository.models import Repository;
class Label(models.Model):
    name = models.CharField(max_length=100,unique=True)
    repo = models.ForeignKey(to=Repository,verbose_name='repo', on_delete=models.CASCADE)
    color = models.CharField(max_length=7, validators=[RegexValidator(regex='^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', message="Color must have a hex value")])

    def __str__(self):
        return self.name 