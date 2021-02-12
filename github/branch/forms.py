from django import forms 
from branch.models import Branch 
  
class BranchForm(forms.ModelForm): 
  
    class Meta: 
        model = Branch 
   
        fields = [ 
            "name"
        ] 