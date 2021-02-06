from . import views
from django.urls import path

app_name = 'milestone'
urlpatterns = [
    path('', views.all_milestones, name='allMilestones'),
    path('add/<id>', views.add_milestone, name='addMilestone'),
    path('update/<id>/<milestone_id>', views.update_milestone, name='updateMilestone'),
    path('delete/<id>/<milestone_id>',views.delete_milestone, name='deleteMilestone')
]