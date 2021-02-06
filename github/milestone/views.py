from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Milestone
from .forms import MilestoneForm
from django.urls import reverse
from  branch.models import Branch
from django.contrib import messages

# Create your views here.

def all_milestones(request):
    milestones = Milestone.objects.all
    context = {'milestones': milestones}
    return render(request, 'milestone/allMilestones.html',context)


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

def update_milestone(request, id, milestone_id):
    context ={}
    obj = get_object_or_404(Milestone, id = milestone_id) 
    form = MilestoneForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def delete_milestone(request, id, milestone_id): 
    context ={} 
    obj = get_object_or_404(Milestone, id = milestone_id)   

    if request.method =="POST":
        obj.delete()
  
    return redirect(reverse("repository:detailRepository",args=(id)))