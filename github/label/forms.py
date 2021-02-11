from django import forms 
from label.models import Label 
  
class LabelForm(forms.ModelForm): 
  
    class Meta: 
        model = Label 
   
        fields = [ 
            "name",
            "color" 
        ] 

        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }