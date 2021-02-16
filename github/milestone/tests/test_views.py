from django.test import TestCase, Client
from django.http import response
from django.urls import reverse
from milestone.models import Milestone
from repository.models import Repository
from wiki.models import Wiki
from project.models import Project
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.all_ms = reverse('milestone:allMilestones')

        test_wiki = Wiki.objects.create(content='test content')
        self.test_repo = Repository.objects.create(name='test repo',wiki_id=test_wiki.id)
        self.test_project = Project.objects.create(name='test project',description='desc', repository_id=self.test_repo.id)

        self.add_ms = reverse('milestone:addMilestone', args=[self.test_repo.id])

    def test_add_milestone_POST(self):
        response = self.client.post(self.add_ms, {
            'title' : 'UKS',
            'description' : 'first milestone',
            'dueDate' : '06/25/21'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Milestone.objects.get(title='UKS').title, 'UKS')

    def test_add_milestone_with_project_POST(self):
        response = self.client.post(self.add_ms, {
            'title' : 'UKS',
            'description' : 'first milestone',
            'dueDate' : '06/25/21',
            'project' : self.test_project
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Milestone.objects.get(title='UKS').title, 'UKS')

    def test_update_milestone_POST(self):
        response = self.client.post(self.add_ms, {
            'title' : 'UKS',
            'description' : 'first milestone',
            'dueDate' : '06/25/21'
        })

        self.assertEquals(Milestone.objects.count(), 1)
        self.assertEquals(Milestone.objects.get(title = 'UKS').title, 'UKS')

        test_ms1 = Milestone.objects.get(title = 'UKS')

        response = self.client.post(reverse('milestone:updateMilestone', args=[self.test_repo.id, test_ms1.id]), {
            'title' : 'new title',
            'description' : 'new desc',
            'dueDate' : '06/30/21'
        })

        self.assertEquals(Milestone.objects.get(title='new title').title, 'new title')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Milestone.objects.count(), 1)

    def test_delete_milestone(self):  
        response = self.client.post(self.add_ms, {
            'title' : 'UKS',
            'description' : 'first milestone',
            'dueDate' : '06/25/21'
        })

        self.assertEquals(Milestone.objects.count(), 1)
        self.assertEquals(Milestone.objects.get(title = 'UKS').title, 'UKS')

        test_ms1 = Milestone.objects.get(title = 'UKS')

        response = self.client.post(reverse('milestone:deleteMilestone', args=[self.test_repo.id, test_ms1.id]))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Milestone.objects.count(), 0)