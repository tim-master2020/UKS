from django.db import models
from wiki.models import Wiki
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    
    photo = models.ImageField(upload_to='images/') 
    users = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
