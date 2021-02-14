from . import views
from django.urls import path


app_name = 'branch'
urlpatterns = [
    path('', views.allBranches, name='allBranches'),
    path('add/<id>', views.addBranch, name='addBranch'),
    path('delete/<id>/<branch_id>', views.delete_view, name='deleteBranch'),
    path('update/<id>/<branch_id>', views.update_view, name='updateBranch'),
    path('<id>/detailBranch', views.detail_view, name='detailBranch'),
    path('createABranchFromExisting/<id>', views.createABranchFromExisting, name='createABranchFromExisting'),
]