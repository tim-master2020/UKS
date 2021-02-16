from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from label.views import all,addLabel,updateLabel,deleteLabel
from label.models import Label
from wiki.models import Wiki
from repository.models import Repository
from django.contrib.auth.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client();

        self.addLabel = reverse('labels:addLabel', args=[1])
        self.deleteLabel = reverse('labels:deleteLabel', args=[1,1])
        self.updateLabel = reverse('labels:updateLabel', args=[1,1])

        self.loggedInUser = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')


    
    def test_add_new_label_withName(self):

        test_wiki = Wiki.objects.create(content='test content')
        test_repo = Repository.objects.create(name='testrepo',wiki_id=test_wiki.id)
        response = self.client.post(reverse('labels:addLabel', args=[test_repo.id]), {
            'name' : 'frontend',
            'color' : '#dcfae4'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.get(name='frontend').name, 'frontend')

    def test_add_new_label_witoutName(self):

        test_wiki = Wiki.objects.create(content='test content')
        test_repo = Repository.objects.create(name='testrepo',wiki_id=test_wiki.id)
        response = self.client.post(reverse('labels:addLabel', args=[test_repo.id]))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Label.objects.all().count(), 0)

    def test_add_new_label_wrongColor(self):

        test_wiki = Wiki.objects.create(content='test content')
        test_repo = Repository.objects.create(name='testrepo',wiki_id=test_wiki.id)
        response = self.client.post(reverse('labels:addLabel', args=[test_repo.id]),{
            'name' : 'frontend',
            'color' : 'wrong'
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Label.objects.all().count(), 0)


    def test_delete_existing_label(self):
        test_wiki = Wiki.objects.create(content='test content')
        test_repo = Repository.objects.create(name='testrepo',wiki_id=test_wiki.id)
        
        response = self.client.post(reverse('labels:addLabel', args=[test_repo.id]),{
            'name' : 'frontend',
            'color' : '#dcfae4'
        })

        test_label = Label.objects.get(name='frontend')
        print('test label id',test_label.id)
        print('test repo id',test_repo.id)
        self.assertEquals(Label.objects.count(), 1)

        response = self.client.post(reverse('labels:deleteLabel',args=[test_repo.id,test_label.id]))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 0)

    def test_update_label(self):
        test_wiki = Wiki.objects.create(content='test content')
        test_repo = Repository.objects.create(name='testrepo',wiki_id=test_wiki.id)
        
        response = self.client.post(reverse('labels:addLabel', args=[test_repo.id]),{
            'name' : 'frontend',
            'color' : '#dcfae4'
        })
        
        test_label = Label.objects.get(name='frontend')

        self.assertEquals(Label.objects.count(), 1)
        self.assertEquals(Label.objects.get(name='frontend').name, 'frontend')

        response = self.client.post(reverse('labels:updateLabel', args=[test_repo.id,test_label.id]),{
            'name' : 'frontend',
            'color' : '#f8fac0'
        })

        self.assertEquals(Label.objects.get(name='frontend').color, '#f8fac0')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 1)