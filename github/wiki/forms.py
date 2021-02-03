from django import forms 
from wiki.models import Wiki 
  
class WikiForm(forms.ModelForm): 
  
    class Meta: 
        model = Wiki 
   
        fields = '__all__'