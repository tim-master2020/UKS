from django import forms 
from repository.models import Repository 
  
class RepositoryForm(forms.ModelForm): 
  
    class Meta: 
        model = Repository 
   
        fields = [ 
            "name" 
        ] 