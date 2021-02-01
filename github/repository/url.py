from . import views
from django.urls import path


app_name = 'repository'
urlpatterns = [
    path('', views.allRepositories, name='allRepositories'),
    path('add', views.addRepository, name='addRepository')
]