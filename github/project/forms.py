from django import forms 
from project.models import Project 
  
class ProjectForm(forms.ModelForm): 
  
    class Meta: 
        model = Project 
   
        fields = [ 
            "name",
            "description"
        ]

class DetailForm(forms.ModelForm):
        
    class Meta: 
       
   
        fields = [ 
            "name",
            "description",
            "tasks"
        ]

        widgets = {
            'task': forms.SelectMultiple(attrs={'required': False})
        } 