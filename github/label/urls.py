from . import views
from django.urls import path

app_name='labels'

urlpatterns = [
    path('all',views.all,name="all"),
]