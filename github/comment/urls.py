from . import views
from django.urls import path


app_name = 'comment'
urlpatterns = [
    path('add/<task_id>',views.addComment, name='addComment'),
    path('delete/<id>',views.deleteComment, name='deleteComment'),
    path('edit/<id>',views.editComment, name='editComment')
]
