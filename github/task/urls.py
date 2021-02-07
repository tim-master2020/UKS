from . import views
from django.urls import path


app_name = 'task'
urlpatterns = [
    path('<id>/',views.detailView, name='detailView'),
    path('add/<repo_id>',views.newTask, name='addTask'),
    path('delete/<id>',views.deleteTask, name='deleteTask'),
]
