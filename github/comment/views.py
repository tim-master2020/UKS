from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from task.models import Task
from django.contrib.auth.models import User
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def addComment(request,task_id):
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            print('Form is valid!',form)
            comment = form.save(commit=False)
            comment.task = Task.objects.get(pk = task_id)
            currentUser = User.objects.get(pk = request.user.id)
            comment.user = currentUser
            comment.save()
            return redirect(reverse("task:detailView",args=(task_id)))
    else:
        return redirect(reverse("task:detailView",args=(task_id)))

@login_required
def deleteComment(request,id):
    print('in delete comment view') 
    comment = get_object_or_404(Comment, id = id)
    task = Task.objects.get(pk = comment.task.id)  
    if request.method =="POST": 
        comment.delete() 
    return redirect(reverse("task:detailView",args=[task.id]))

@login_required
def editComment(request,id):

    if request.method == "GET":
        comment = get_object_or_404(Comment, id = id) 
        form = CommentForm(instance = comment) 
        return render(request,'comments/edit-comment.html',{'form':form,'id':comment.id,'task_id':comment.task.id})

    if request.method == "POST":
        print('in edit post')
        obj = get_object_or_404(Comment, id = id)
        form = CommentForm(request.POST or None,request.FILES, instance = obj)
        if form.is_valid(): 
            form.save()
            return redirect(reverse("task:detailView",args=[obj.task.id]))
        else:
            print('not valid form when updating!',form.errors)

