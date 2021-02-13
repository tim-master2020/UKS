from django.shortcuts import render
from .forms import CommitForm
from django.contrib import messages
from django.urls import reverse
from .models import Commit
from django.contrib.auth.models import User
import random
import string
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 

def all_commits(request):
    commits = Commit.objects.all
    context = {'allCommits': commits}
    return render(request, 'commits/allCommits.html',context)

def add_commit(request, id):
    if request.method == 'POST':
        form = CommitForm(request.POST)

        if form.is_valid():
            commit = form.save(commit=False)
            commit.branch_id = id
            letters_and_digits = string.ascii_letters + string.digits
            result_str = ''.join((random.choice(letters_and_digits) for i in range(7)))
            commit.sha = result_str.lower()
            currentUser = User.objects.get(pk = request.user.id)
            commit.user = currentUser
            commit.save()
            messages.success(request, 'You successfully created a new commit')
            return redirect(reverse("branch:detailBranch",args=(id)))
        else:
            print('Form is not valid!')

    else:
        form = CommitForm()

    return render(request, 'commit/addCommit.html', {'form': form})