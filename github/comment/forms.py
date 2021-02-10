from django import forms 
from .models import Comment 
  
class CommentForm(forms.ModelForm): 
  
    class Meta: 
        model = Comment 
        fields = [ 
            'text'
        ]

        widgets = {
            'text' : forms.Textarea(),
        }

    def __init__(self, *args, **kwargs): 
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Leave a comment'