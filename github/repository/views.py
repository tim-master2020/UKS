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
