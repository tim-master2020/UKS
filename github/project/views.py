from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect) 
from .models import Project
from .forms import ProjectForm
from django.urls import reverse
from  branch.models import Branch
from django.contrib import messages
from django.http import HttpResponse
from task.models import Task
from repository.models import Repository
from milestone.models import Milestone
from django.core.cache import cache

def project_key(id):
    return "project."+str(id)

def projects_key():
    return "project.all."

def all_projects(request):
    projects = get_projects_from_cache()
    context = {'allProjects': projects}
    return render(request, 'project/allProjects.html',context)


def add_project(request, id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.repository_id = id
            project.save()
            messages.success(request, 'You successfully created a new project')
            return redirect(reverse("repository:detailRepository",args=(id)))
        else:
            print('Form is not valid!')

    else:
        form = ProjectForm()

    return render(request, 'project/addProject.html', {'form': form})

def update_project(request, id, project_id):
    context ={}
    project = get_project_from_cache(project_id)
    if not project:
        return redirect(reverse("repository:detailRepository",args=(id)))

    form = ProjectForm(request.POST or None, instance = project) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def delete_project(request, id, project_id): 
    context ={} 
    project = get_project_from_cache(project_id)
    if not project:
        return redirect(reverse("repository:detailRepository",args=(id))) 

    if request.method =="POST":
        project.delete()
        remove_project_from_cache(project_id)
  
    return redirect(reverse("repository:detailRepository",args=(id)))

def add_tasks(request, project_id):
    selectedTasks = request.POST.getlist("tasks")
    project = get_project_from_cache(project_id)
    if not project:
        return redirect(reverse("project:detailProject",args=[project.id]))

    repo = Repository.objects.get(id = project.repository_id)  
    
    for item in selectedTasks:
        task = Task.objects.get(id = item)
        task.project.add(project)
        task.save()
    return redirect(reverse("project:detailProject",args=[project.id]))

def add_milestones(request, project_id):
    selectedMs = request.POST.getlist("milestones")
    project = get_project_from_cache(project_id)
    if not project:
        return redirect(reverse("project:detailProject",args=[project.id]))
    repo = Repository.objects.get(id = project.repository_id)  
    
    for item in selectedMs:
        milestone = Milestone.objects.get(id = item)
        milestone.project.add(project)
        milestone.save()
    return redirect(reverse("project:detailProject",args=[project.id]))

def project_detail(request, project_id): 
    context ={} 
    
    newTasks = []
    existingTasks = []

    obj = get_project_from_cache(project_id)
    milestones = Milestone.objects.filter(repository_id = obj.repository_id)
    
    existingMs = []
    newMs = []
    for ms in milestones:
        if obj in ms.project.all():
            existingMs.append(ms)
        else:
            newMs.append(ms)
    
    context["existingMs"] = existingMs
    context["newMs"] = newMs

    tasks = Task.objects.filter(repo_id = obj.repository_id)
    for task in tasks:
        if obj in task.project.all():
            existingTasks.append(task)
        else:
            newTasks.append(task)

    context["newTasks"] = newTasks
    context["existingTasks"] = existingTasks
    context["projectData"] = get_project_from_cache(project_id)

    return render(request, "project/detailProject.html", context)

def get_project_from_cache(project_id):
    project = cache.get(project_key(project_id))
    if not project:
        try:
            project = Project.objects.get(id=project_id)
        except:
            return None
        cache.set(project_key(project_id), project)
    return project

def get_projects_from_cache():
    projects = cache.get(projects_key)
    if not projects:
        try:
            projects = Project.objects.all()
        except:
            return None
        cache.set(projects_key, projects)
    return projects

def remove_project_from_cache(project_id):
    cache.delete(project_key(project_id))
