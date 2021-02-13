from . import views
from django.urls import path

app_name = 'commit'
urlpatterns = [
    path('add/<id>', views.add_commit, name='addCommit')
]