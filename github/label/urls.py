from . import views
from django.urls import path

urlpatterns = [
    path('all',views.all,name="all"),
]