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
    
    def test_add_new_repository_no_members(self):
        response = self.client.post(self.addRepository, {
            'name' : 'UKS',
            'user' : ['Choose members']
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Repository.objects.get(name='UKS').name, 'UKS')

    def test_add_new_repository_withMembers(self):
        member = User.objects.create_user(username='testmember', password='12345')
        response = self.client.post(self.addRepository, {
            'name' : 'UKS1',
            'user' : ['testmember']
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Repository.objects.get(name='UKS1').name, 'UKS1')

    def test_add_new_repository_check_is_master_branch_created(self):
        response = self.client.post(self.addRepository, {
            'name' : 'UKS2',
            'user' : ['Choose members']
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Repository.objects.get(name='UKS2').name, 'UKS2')
        self.assertEquals(Branch.objects.get(name='master').name, 'master')

    def test_delete_existing_repository(self):
        response = self.client.post(self.addRepository, {
            'name' : 'repo',
            'user' : ['Choose members']
        })

        self.assertEquals(Repository.objects.count(), 1)

        response = self.client.post(self.deleteRepository)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Repository.objects.count(), 0)

    