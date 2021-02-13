from django import forms 
from commit.models import Commit 
  
class CommitForm(forms.ModelForm): 
  
    class Meta: 
        model = Commit 
   
        fields = [ 
            "message"
        ]