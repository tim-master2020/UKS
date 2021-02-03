from . import views
from django.urls import path

app_name='labels'

urlpatterns = [
    path('all',views.all,name="all"),
    path('add/<id>',views.addLabel,name="addLabel"),
    path('update/<id>/<label_id>',views.updateLabel,name="updateLabel"),
    path('delete/<id>/<label_id>',views.deleteLabel,name="deleteLabel"),
]
