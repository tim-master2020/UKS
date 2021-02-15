from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from github.views import register, profile, login
from user.views import editUser
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register = reverse('register')
        self.profile = reverse('profile')
        self.login = reverse('login')
    
    def test_register(self):
        response = self.client.post(self.register, {
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra1234567!',
            'email' : 'email@gmail.com'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='Korisnik').username, 'Korisnik')
        
    def test_profile(self):
        createUser = User.objects.create_user(username='test', password='Sifra1234567!')
        login = self.client.login(username='test', password='Sifra1234567!')
        response = self.client.get(self.profile)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_login(self):
        createUser = User.objects.create_user(username='Korisnik', password='Sifra1234567!')
        response = self.client.post(self.login, {
            'username' : 'Korisnik',
            'password' : 'Sifra1234567!'
        })

        self.assertEquals(response.status_code, 302)