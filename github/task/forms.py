from django import forms 
from django.forms import ModelForm
from task.models import Task
from crispy_forms.helper import FormHelper 
from label.models import Label
from project.models import Project
from milestone.models import Milestone
 
class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        if 'repo_id' in kwargs:
            repo_id = kwargs.pop('repo_id')
            self.fields['labels'].queryset = Label.objects.filter(repo_id = repo_id)
            self.fields['project'].queryset = Project.objects.filter(repository_id = repo_id)
            self.fields['milestone'].queryset = Milestone.objects.filter(repository_id = repo_id)
            self.fields['asignees'].queryset = Repository.objects.get(pk = repo_id).users.all()

    class Meta: 
        model = Task
           
        fields = [ 
            "title",
            "description",
            "taskStatus",
            "taskState",
            "taskPriorty",
            "taskType",
            "labels",
            "asignees",
            "milestone",
            "project",
        ]

        widgets = {
            'description': forms.Textarea(),
            'asignees': forms.CheckboxSelectMultiple(attrs={'required': False}),
            'project': forms. SelectMultiple(attrs={'required': False}),
            "title" : forms.TextInput(attrs={'required': True}),
            'labels': forms.SelectMultiple(attrs={'required': False}),
            'milestone': forms.SelectMultiple(attrs={'required': False})
        }



