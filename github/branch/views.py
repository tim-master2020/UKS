from django.db.models import base
from django.http.response import HttpResponse
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Repository
from  branch.models import Branch
from  commit.models import Commit
from django.contrib import messages
from .forms import BranchForm
from django.contrib.auth.models import User
from django.urls import reverse


def allBranches(request):
    repoId = request.path.split("/")[2]
    allBranches = Branch.objects.filter(repository_id=repoId)
    context = {'allBranches': allBranches}
    return render(request, "branch/allBranches.html", context)

def addBranch(request, id):
    if request.method == 'POST':
        form = BranchForm(request.POST)

        if form.is_valid():
            branch = form.save(commit=False)
            branch.repository_id = id
            branch.baseBranch = 'master'
            branch.save()

            messages.success(request, 'You successfully created a new branch')
            return redirect(reverse("repository:detailRepository",args=(id)))
        else:
            print('Form is not valid!')

    else:
        form = BranchForm()

    return render(request, 'branch/addBranch.html', {'form': form})

def delete_view(request, branch_id, id): 
    obj = get_object_or_404(Branch, id = branch_id)   

    if request.method =="POST":
        obj.delete()
  
    return redirect(reverse("repository:detailRepository",args=(id)))

def update_view(request, id, branch_id):  
    context ={}
    obj = get_object_or_404(Branch, id = branch_id) 
    form = BranchForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def createABranchFromExisting(request, id):
    baseBranch = get_object_or_404(Branch, id = id)
    baseBranchName = baseBranch.name
    repo = Repository.objects.get(id = baseBranch.repository_id)
    form = BranchForm(request.POST)
    if form.is_valid(): 
        branch = form.save(commit=False)
        branch.repository_id = repo.id
        branch.baseBranch = baseBranchName
        branch.save()
        return redirect(reverse("repository:detailRepository", args=[repo.id]))
    else:
        return redirect(reverse("repository:detailRepository", args=[repo.id]))

def detail_view(request, id): 
    context ={}
    context["branchData"] = Branch.objects.get(id = id)
    context["allCommits"] = Commit.objects.filter(branch_id = id)
    return render(request, "branch/detailBranch.html", context)
