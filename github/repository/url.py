from . import views
from django.urls import path


app_name = 'repository'
urlpatterns = [
    path('', views.allRepositories, name='allRepositories'),
    path('add', views.addRepository, name='addRepository'),
    path('<id>/delete', views.delete_view, name='deleteRepository'),
    path('<id>/update', views.update_view, name='updateRepository'),
]