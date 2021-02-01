from django import forms 
from repository.models import Repository 
  
  
# creating a form 
class RepositoryForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Repository 
  
        # specify fields to be used 
        fields = [ 
            "name" 
        ] 