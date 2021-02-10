from . import views
from django.urls import path

app_name = 'project'
urlpatterns = [
    path('', views.all_projects, name='allProjects'),
    path('add/<id>', views.add_project, name='addProject'),
    path('update/<id>/<project_id>', views.update_project, name='updateProject'),
    path('delete/<id>/<project_id>',views.delete_project, name='deleteProject'),
    path('addTasks/<project_id>',views.add_tasks, name='addTasks'),
    path('addMilestones/<project_id>', views.add_milestones, name='addMilestones'),
    path('<project_id>/detailProject', views.project_detail, name='detailProject')
]