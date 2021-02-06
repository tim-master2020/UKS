from django import forms 
from milestone.models import Milestone 
  
class MilestoneForm(forms.ModelForm): 
  
    class Meta: 
        model = Milestone 
   
        fields = [ 
            "title",
            "description",
            "dueDate"
        ]