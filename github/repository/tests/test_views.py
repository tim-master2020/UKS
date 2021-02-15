from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from repository.views import allRepositories, addRepository, delete_view, update_view, detail_view
from repository.models import Repository
from branch.models import Branch
from django.contrib.auth.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client();

        self.allRepositoriesUrl = reverse('repository:allRepositories')
        self.addRepository = reverse('repository:addRepository')
        self.deleteRepository = reverse('repository:deleteRepository', args=[4])
        self.deleteRepositoryNoId = reverse('repository:deleteRepository', args=[11])
        self.updateRepository = reverse('repository:updateRepository', args=[5])

        self.loggedInUser = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_allRepositories_GET(self):
        response = self.client.get(self.allRepositoriesUrl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'repository/allRepositories.html')
    

    
