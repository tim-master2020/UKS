from django import forms 
from .models import Comment 
from django.forms.widgets import ClearableFileInput,CheckboxInput,FileInput
from django.utils.html import conditional_escape,escape
from django.utils.safestring import mark_safe
class CustomFileInput(ClearableFileInput):
    template_with_initial = u'%(initial)s<br /> %(clear_template)s<br />%(input_text)s:<br /> %(input)s'

    def render(self, name, value, attrs=None, renderer=None):
        substitutions = {
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = u'%(input)s'
        substitutions['input'] = FileInput().render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = (u'<a href="%s" width="60" target="_blank" height="60">%s</a>'
                                        % (escape(value.url),(escape(value.url.split('/')[3]))))

        return mark_safe(template % substitutions)
  
class CommentForm(forms.ModelForm): 
  
    class Meta: 
        model = Comment 
        fields = [ 
            'text',
            'file'
        ]

        widgets = {
            'file' : CustomFileInput(),
            'text' : forms.Textarea(),
            
        }

    def __init__(self, *args, **kwargs): 
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Leave a comment'
        if self.instance is not None:
            self.fields['file'].label = ''