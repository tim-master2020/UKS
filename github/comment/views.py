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

# Create your views here.

def addComment(request,task_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
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

