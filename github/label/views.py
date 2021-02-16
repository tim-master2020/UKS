from django.shortcuts import render
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse
from urllib.parse import urlencode
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Label
from .forms import LabelForm
from repository.models import Repository
from repository.views import detail_view
from django.core.exceptions import ValidationError

def all(request):
    labels = Label.objects.all
    context = {'all_labels': labels}
    return render(request, 'label/all-labels.html',context)

def addLabel(request,id):
    context = {}
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            label = form.save(commit=False)
            label.repo = Repository.objects.get(pk = id)
            label.save()
            return redirect(reverse("repository:detailRepository",args=(id)))
        else:
            print('Form is not valid!')

    if request.method == 'GET':
        form = LabelForm()
    
    context["form"] = form     
    return render(request, 'label/add-label.html',{'form':form,'id':id})

def updateLabel(request,id,label_id):
    context ={}
    obj = get_object_or_404(Label, id = label_id) 
    form = LabelForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def deleteLabel(request, id,label_id): 
    context ={} 
    obj = get_object_or_404(Label, id = label_id)   

    if request.method =="POST": 
        obj.delete()
  
    return redirect(reverse("repository:detailRepository",args=(id)))