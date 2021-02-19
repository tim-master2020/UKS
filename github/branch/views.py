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
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

def branch_key(id):
    return "branch."+str(id)

def branches_key(repo_id):
    return "branches.all."+str(repo_id)

def get_branch_from_cache(branch_id):
    branch = cache.get(branch_key(branch_id))
    if not branch:
        try:
            branch = Branch.objects.get(id=branch_id)
        except:
            return None
        cache.set(branch_key(branch_id), branch)
    return branch

def remove_branch_from_cache(branch_id):
    cache.delete(branch_key(branch_id))

def get_branches_from_cache(repo_id):
    branches = cache.get(branches_key(repo_id))
    
    if not branches:
        branches = Branch.objects.filter(repository_id=repo_id)
        cache.set(branches_key(repo_id),branches)

    return branches

def allBranches(request):
    repoId = request.path.split("/")[2]
    allBranches = get_branches_from_cache(repoId)
    if not allBranches:
            return redirect(reverse("repository:detailRepository",args=[repoId]))
    context = {'allBranches': allBranches}
    return render(request, "branch/allBranches.html", context)

@login_required
def addBranch(request, id):
    if request.method == 'POST':
        form = BranchForm(request.POST)

        if form.is_valid():
            branch = form.save(commit=False)
            branch.repository_id = id
            branch.baseBranch = 'master'+str(branch.repository_id)
            branch.save()

            messages.success(request, 'You successfully created a new branch')
            return redirect(reverse("repository:detailRepository",args=(id)))
        else:
            print('Form is not valid!')

    else:
        form = BranchForm()

    return render(request, 'branch/addBranch.html', {'form': form})

@login_required
def delete_view(request, branch_id, id): 
    obj = get_object_or_404(Branch, id = branch_id)  
    branch = get_branch_from_cache(branch_id)
     
    if not branch:
        return redirect(reverse("repository:detailRepository",args=(id))) 

    if request.method =="POST":
        obj.delete()
        remove_branch_from_cache(branch_id)
  
    return redirect(reverse("repository:detailRepository",args=(id)))

@login_required
def update_view(request, id, branch_id):  
    context ={}
    branch = get_branch_from_cache(branch_id)
    if not branch:
        return redirect(reverse("repository:detailRepository",args=[id]))
    form = BranchForm(request.POST or None, instance = branch,repo_id=id)
    if form.is_valid(): 
        form.save()
        return redirect(reverse("repository:detailRepository",args=[id]))

@login_required
def createABranchFromExisting(request, id):
    print('base branch id is',id);
    baseBranch = get_object_or_404(Branch, id = id)
    baseBranchName = baseBranch.name
    print('base branch name is',baseBranchName);
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
