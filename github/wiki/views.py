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
from django.core.cache import cache

def wiki_key(id):
    return "wiki."+str(id)

def detail_view(request, id): 
    context ={} 
    wiki = get_wiki_from_cache(id)
    context["wiki"] = wiki
    
    return render(request, "wiki/wiki.html", context)


def update_view(request, id):  
    context ={} 
   
    wiki = get_wiki_from_cache(id)
    if not wiki:
        return redirect(reverse("repository:detailRepository",args=[repo[0].id]))

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

def get_wiki_from_cache(wiki_id):
    wiki = cache.get(wiki_key(wiki_id))
    if not wiki:
        try:
            wiki = Wiki.objects.get(id=wiki_id)
        except:
            return None
        cache.set(wiki_key(wiki_id),wiki)
    return wiki