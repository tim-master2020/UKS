from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from repository.models import Repository
from label.models import Label
from project.models import Project
from comment.models import Comment
from comment.forms import CommentForm

from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse

def detailView(request, id,form = None): 
    if request.method == 'GET':
        print('in get')
        context ={} 
        task = Task.objects.get(pk = id);
        repo_id = task.repo_id
        asignees = task.asignees.all();
        form = TaskForm(
        {'title':task.title,
        'description':task.description,
        'taskStatus':task.taskStatus,
        'taskState':task.taskState,
        'taskPriorty':task.taskPriorty,
        'taskType':task.taskType,
        'labels':[label for label in task.labels.values_list('id', flat=True)],
        'asignees':[user for user in task.asignees.values_list('id', flat=True)],
        'milestone':[milestone for milestone in task.milestone.values_list('id', flat=True)],
        'project':[project for project in task.project.values_list('id', flat=True)]},
        repo_id = repo_id,)

        comments = Comment.objects.filter(task_id = id)
        commentForm = CommentForm()

        return render(request, "task/detail-task.html", {'form': form,'repo_id':repo_id,'task_id':id,'comments':comments,'commentForm':commentForm,'currentUser':request.user})
        
    if request.method == 'POST':
        obj = get_object_or_404(Task, id = id)
        print('obj at update',obj) 
        form = TaskForm(request.POST or None, instance = obj,repo_id=obj.repo_id)
        if form.is_valid(): 
            form.save()
            return redirect(reverse("repository:detailRepository",args=[obj.repo_id]))
        else:
            print('not valid form when updating!',form.errors)

def newTask(request,repo_id): 
    print('in new task view');
    if request.method == 'GET':
        print('in new task view GET'); 
        form = TaskForm(repo_id = repo_id)
        return render(request, "task/detail-task.html", {'form': form,'repo_id':repo_id,'is_adding':True})

    if request.method == 'POST':
        print('in new task view POST');
        print('request is',request)
        form = TaskForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            task = form.save(commit=False)
            task.repo = Repository.objects.get(pk = repo_id)
            currentUser = User.objects.get(pk = request.user.id)
            task.author = currentUser

            task.save()
            form.save_m2m()

            print('currently creating this task',task.labels.all())
            
            return redirect(reverse("repository:detailRepository",args=(repo_id)))
        else:
            print('Form is not valid!')
    
def deleteTask(request,id):
    context ={} 
    obj = get_object_or_404(Task, id = id)
    repo = Repository.objects.get(name = obj.repo)  
    if request.method =="POST": 
        obj.delete() 
    return redirect(reverse("repository:detailRepository",args=[repo.id]))



