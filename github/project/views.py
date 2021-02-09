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

# Create your views here.

def all_projects(request):
    projects = Project.objects.all
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
    obj = get_object_or_404(Project, id = project_id) 
    form = ProjectForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        return redirect(reverse("repository:detailRepository",args=(id)))
    else:
        return redirect(reverse("repository:detailRepository",args=(id)))

def delete_project(request, id, project_id): 
    context ={} 
    obj = get_object_or_404(Project, id = project_id)   

    if request.method =="POST":
        obj.delete()
  
    return redirect(reverse("repository:detailRepository",args=(id)))

def add_tasks(request, project_id):
    selectedTasks = request.POST.getlist("tasks")
    obj = get_object_or_404(Project, id = project_id)
    repo = Repository.objects.get(id = obj.repository_id)  
    
    for item in selectedTasks:
        task = Task.objects.get(id = item)
        task.project.add(obj)
        task.save()
    return redirect(reverse("project:detailProject",args=[obj.id]))

def project_detail(request, project_id): 
    context ={} 
    newTasks = []
    resTasks = []
    tasks = Task.objects.all()
    for task in Task.objects.all():
        for project in task.project.all():
            if str(project.id)==str(project_id):
                newTasks.append(task)
    for task in Task.objects.all():
        if task not in newTasks:
            resTasks.append(task)
    context["newtasks"] = resTasks
    context["projectData"] = Project.objects.get(id = project_id) 
    return render(request, "project/detailProject.html", context)


