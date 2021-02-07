from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from repository.models import Repository
from label.models import Label
from project.models import Project

from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse

def detailView(request, id): 
    if request.method == 'GET':
        context ={} 
        task = Task.objects.get(pk = id);
        repo_id = task.repo_id
        asignees = task.asignees.all();
        form = TaskForm({'title':task.title,'description':task.description,'taskStatus':task.taskStatus,'taskState':task.taskState,'taskPriorty':task.taskPriorty,'taskType':task.taskType,
        'labels':[label for label in task.labels.values_list('id', flat=True)],
        'asignees':[user for user in task.asignees.values_list('id', flat=True)],
        'milestone':task.milestone,
        'project':[project for project in task.project.values_list('id', flat=True)],
        'repo_id':repo_id})

        return render(request, "task/detail-task.html", {'form': form,'repo_id':repo_id,'task_id':id})
        
    if request.method == 'POST':
        obj = get_object_or_404(Task, id = id) 
        form = TaskForm(request.POST or None, instance = obj)
        print('labels',obj.labels.all()) 
        if form.is_valid(): 
            form.save()
            return redirect(reverse("repository:detailRepository",args=[obj.repo_id]))
        else:
            print('not valid form when updating!',form.errors)


# Create your views here.
