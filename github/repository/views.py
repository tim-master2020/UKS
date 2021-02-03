from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Repository
from  branch.models import Branch
from django.contrib import messages
from .forms import RepositoryForm
from .forms import RepositoryForm
from wiki.models import Wiki
from django.contrib.auth.models import User


def allRepositories(request):
    allRepositories = Repository.objects.filter(user_id=request.user.id)
    #treba pristupiti brancount polju iz svakog repozitorijuma i staviti mu vrednost iz baze i takve objekte sacuvati u allRepositories
    branchCount = Branch.objects.all()
    context = {'allRepositories': allRepositories, 'branchCount' : branchCount}
    return render(request, "repository/allRepositories.html", context)

def addRepository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)

        if form.is_valid():
            repo = form.save(commit=False)

            wiki = Wiki(content="")
            wiki.save();

            repo.wiki = wiki;

            currentUser = User.objects.get(id = request.user.id)
            repo.user = currentUser; 
            repo.save();

            messages.success(request, 'You successfully created a new repository')
            return redirect('/repository')
        else:
            print('Form is not valid!')

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
           
    return render(request, "repository/detailRepository.html", context)
