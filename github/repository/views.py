from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Repository, Wiki
from project.models import Project
from label.models import Label
from milestone.models import Milestone
from  branch.models import Branch
from django.contrib import messages
from .forms import RepositoryForm
from .forms import RepositoryForm
from django.contrib.auth.models import User
from task.models import Task
from label.forms import LabelForm
from photo.models import Photo


def allRepositories(request):
    allRepositories = Repository.objects.filter(users=request.user.id)
    #treba pristupiti brancount polju iz svakog repozitorijuma i staviti mu vrednost iz baze i takve objekte sacuvati u allRepositories
    branchCount = Branch.objects.all()

    allUsers = User.objects.exclude(username=request.user)
    print(allUsers)
    context = {'allRepositories': allRepositories, 'branchCount' : branchCount, 'allUsers': allUsers}
    return render(request, "repository/allRepositories.html", context)

def addRepository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)

        if form.is_valid():
            repo = form.save(commit=False)

            wiki = Wiki(content="")
            wiki.save()

            repo.wiki = wiki

            repo.save()

            currentUser = User.objects.get(id = request.user.id)
            repo.users.add(currentUser)

            selectedUsers = request.POST.getlist('user', None)
            if (not selectedUsers[0] == 'Choose members'):
                for item in selectedUsers:
                    member = User.objects.get(username=item)
                    repo.users.add(member)
            
            branch = Branch(name="master", repository_id=repo.id)
            branch.save()

            messages.success(request, 'You successfully created a new repository')
            return redirect('/repository')
        else:
            print('Form is not valid!')
            print(form)

    else:
        form = RepositoryForm()

    return render(request, 'repository/addRepository.html', {'form': form})

def delete_view(request, id): 
    context ={} 
  
    obj = get_object_or_404(Repository, id = id) 
  
  
    if request.method =="POST": 
 
        obj.delete()
        return HttpResponseRedirect("/repository") 
  
    return HttpResponseRedirect("/repository")

def update_view(request, id):  
    context ={} 
   
    obj = get_object_or_404(Repository, id = id) 

    form = RepositoryForm(request.POST or None, instance = obj) 
    
    if form.is_valid():
        form.save() 
        return HttpResponseRedirect("/repository") 
  
    context["form"] = form 
  
    return render(request, "allRepositories.html", context)

def detail_view(request, id): 
    context ={} 

    context["repoData"] = Repository.objects.get(id = id)   
    context["tasks"] = Task.objects.filter(repo_id = id)
    context["allProjects"] = Project.objects.filter(repository_id = id).order_by('-name')
    context["milestones"] = Milestone.objects.filter(repository_id = id).order_by('title')
    context["allBranches"] = Branch.objects.filter(repository_id=id).order_by('-name')
    
    context["addLabelForm"] = LabelForm() 
    labels = []
    for label in Label.objects.filter(repo_id = id).order_by('-name'):
        labels.append(LabelForm(instance=label))
    context['labels'] = labels;

    tasksAssignes = {}
    for t in Task.objects.filter(repo_id = id):
        photos = []
        for a in t.asignees.all():
            photos.append( None if not Photo.objects.filter(users_id = a.id) else Photo.objects.filter(users_id = a.id)[0])
        tasksAssignes[t.id] = photos
    context['tasks_assignes'] = tasksAssignes;
    print('task assinges',tasksAssignes)


    return render(request, "repository/detailRepository.html", context)
