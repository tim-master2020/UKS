from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from repository.models import Repository
from label.models import Label
from project.models import Project
from comment.models import Comment
from comment.forms import CommentForm
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse

def task_key(id):
    return "task."+str(id)

def detailView(request, id,form = None): 
    if request.method == 'GET':
        print('in get')
        context ={} 
        task = get_task_from_cache(id)
        if not task:
            return redirect(reverse("repository:detailRepository",args=[task.repo_id]))
        repo_id = task.repo_id
        asignees = task.asignees.all()
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
        task = get_task_from_cache(id)
        if not task:
            return redirect(reverse("repository:detailRepository",args=[task.repo_id]))
        print('obj at update',task) 
        form = TaskForm(request.POST or None, instance = task,repo_id=task.repo_id)
        if form.is_valid(): 
            form.save()
            return redirect(reverse("repository:detailRepository",args=[task.repo_id]))
        else:
            print('not valid form when updating!',form.errors)

@login_required
def newTask(request,repo_id): 

    if request.method == 'GET':
        print('in new task view GET'); 
        form = TaskForm(repo_id = repo_id)
        return render(request, "task/detail-task.html", {'form': form,'repo_id':repo_id,'is_adding':True})

    if request.method == 'POST':
        print('in new task view POST')
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
    
@login_required
def deleteTask(request,id):
    context ={} 
    task = get_task_from_cache(id)
     
    if not task:
        repo = Repository.objects.get(name = task.repo)
        return redirect(reverse("repository:detailRepository",args=(repo.id)))
    repo = Repository.objects.get(name = task.repo) 
    if request.method =="POST": 
        task.delete()
        remove_task_from_cache(id) 
    return redirect(reverse("repository:detailRepository",args=[repo.id]))

def get_task_from_cache(task_id):
    task = cache.get(task_key(task_id))
    if not task:
        try:
            task = Task.objects.get(id=task_id)
        except:
            return None
        cache.set(task_key(task_id), task)
    return task

def remove_task_from_cache(task_id):
    cache.delete(task_key(task_id))

