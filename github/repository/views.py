from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Repository
from  branch.models import Branch
from django.contrib import messages
from .forms import RepositoryForm
from .forms import RepositoryForm


def allRepositories(request):
    allRepositories = Repository.objects.all()
    #treba pristupiti brancount polju iz svakog repozitorijuma i staviti mu vrednost iz baze i takve objekte sacuvati u allRepositories
    branchCount = Branch.objects.all()
    context = {'allRepositories': allRepositories, 'branchCount' : branchCount}
    return render(request, "repository/allRepositories.html", context)

def addRepository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            form.save()
            messages.success(request, 'You successfully created a new repository')
            return redirect('/repository')
        else:
            print('Form is not valid!')

    else:
        form = RepositoryForm()

    return render(request, 'repository/addRepository.html', {'form': form})

def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Repository, id = id) 
  
  
    if request.method =="POST": 
        #delete object 
        obj.delete() 
        #after deleting redirect to  
        #home page 
        return HttpResponseRedirect("/repository") 
  
    return HttpResponseRedirect("/repository")

# update view for details 
def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Repository, id = id) 
  
    # pass the object as instance in form 
    form = RepositoryForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/repository") 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "allRepositories.html", context)

def detail_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
   
    # add the dictionary during initialization 
    context["repoData"] = Repository.objects.get(id = id) 
           
    return render(request, "repository/detailRepository.html", context)
