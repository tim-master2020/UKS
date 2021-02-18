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
from django.core.cache import cache

def labels_key():
    return "labels.all."

def label_key(id):
    return "label."+str(id)

def all(request):
    labels = get_labels_from_cache()
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
    label = get_label_from_cache(label_id)
    if not label:
        return redirect(reverse("repository:detailRepository",args=(id)))

    form = LabelForm(request.POST or None, instance = label) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def deleteLabel(request, id,label_id): 
    context ={} 
    label = get_label_from_cache(label_id)  

    if not label:
        return redirect(reverse("repository:detailRepository",args=(id))) 

    if request.method =="POST": 
        label.delete()
        remove_label_from_cache(label_id)
  
    return redirect(reverse("repository:detailRepository",args=(id)))

def get_labels_from_cache():
    labels = cache.get(labels_key())
    if not labels:
        try:
            labels = Label.objects.all()
        except:
            return None
        cache.set(labels_key, labels)

    return labels

def get_label_from_cache(label_id):
    label = cache.get(label_key(label_id))
    if not label:
        try:
            label = Label.objects.get(id=label_id)
        except:
            return None
        cache.set(label_key(label_id), label)
    return label   

def remove_label_from_cache(label_id):
    cache.delete(label_key(label_id)) 