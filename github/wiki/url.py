from . import views
from django.urls import path

app_name = 'wiki'
urlpatterns = [
    path('<id>', views.detail_view, name='viewWiki'),
    path('<id>/update', views.update_view, name='updateWiki'),
]