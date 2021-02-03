from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse
from .models import Wiki
from repository.models import Repository
from  branch.models import Branch
from django.contrib import messages
from .forms import WikiForm

# Create your views here.

def detail_view(request, id): 
    context ={} 

    context["wiki"] = Wiki.objects.get(id = id) 
    
    return render(request, "wiki/wiki.html", context)


def update_view(request, id):  
    context ={} 
   
    obj = get_object_or_404(Wiki, id = id) 
    form = WikiForm(request.POST or None, instance = obj)

    if form.is_valid():
        wiki = form.save(commit=False)
        if not form.cleaned_data['content']:
            wiki.content = ""
        
        wiki.save()
        repo = Repository.objects.filter(wiki_id = id)
        return redirect(reverse("repository:detailRepository",args=[repo[0].id]))
  
    context['form'] = form
  
    return render(request, "wiki/wiki.html", context)