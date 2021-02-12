from . import views
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('edit/',views.editUser, name='editUser')
]
