from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Milestone
from .forms import MilestoneForm
from django.urls import reverse
from  branch.models import Branch
from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

def milestone_key(id):
    return "milestone."+str(id)

def milestones_key():
    return "milestones.all."

def all_milestones(request):
    milestones = get_milestones_from_cache()
    context = {'milestones': milestones}
    return render(request, 'milestone/allMilestones.html',context)

@login_required
def add_milestone(request, id):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)

        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.repository_id = id
            milestone.save()
            messages.success(request, 'You successfully created a new milestone')
            return redirect(reverse("repository:detailRepository",args=(id)))
        else:
            print('Form is not valid!')

    else:
        form = MilestoneForm()

    return render(request, 'milestone/addMilestone.html', {'form': form})

@login_required
def update_milestone(request, id, milestone_id):
    context ={}
    milestone = get_milestone_from_cache(milestone_id)
    if not milestone:
        return redirect(reverse("repository:detailRepository",args=(id)))

    form = MilestoneForm(request.POST or None, instance = milestone) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

@login_required
def delete_milestone(request, id, milestone_id): 
    context ={} 
    milestone = get_milestone_from_cache(milestone_id)
    if not milestone:
        return redirect(reverse("repository:detailRepository",args=(id)))  

    if request.method =="POST":
        milestone.delete()
        remove_milestone_from_cache(milestone_id)
  
    return redirect(reverse("repository:detailRepository",args=(id)))

def get_milestone_from_cache(milestone_id):
    milestone = cache.get(milestone_key(milestone_id))
    if not milestone:
        try:
            milestone = Milestone.objects.get(id=milestone_id)
        except:
            return None
        cache.set(milestone_key(milestone_id), milestone)
    return milestone

def get_milestones_from_cache():
    milestones = cache.get(milestones_key)
    if not milestones:
        try:
            milestones = Milestone.objects.all()
        except:
            return None
        cache.set(milestones_key, milestones)
    return milestones

def remove_milestone_from_cache(milestone_id):
    cache.delete(milestone_key(milestone_id))