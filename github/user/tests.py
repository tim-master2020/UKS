from user.forms import UserForm, UserUpdateForm
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from github.views import register, profile
from user.views import editUser
from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from github.views import register, profile, login
from user.views import editUser
import json

class TestForms(TestCase):
    def test_user_form_is_valid(self):
        form = UserForm(data={
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra1234567!',
            'email' : 'email@gmail.com'
        })

        self.assertTrue(form.is_valid())
    
    def test_edit_form_is_valid(self):
        form = UserUpdateForm(data={
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'email' : 'email@gmail.com'
        })

        self.assertTrue(form.is_valid())
    
    def test_user_form_is_not_valid(self):
        form = UserForm(data={})

        self.assertFalse(form.is_valid())
    
    def test_user_without_first_name_is_not_valid(self):
        form = UserForm(data={
            'username' : 'Korisnik',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra1234567!',
            'email' : 'email@gmail.com'
        })

        self.assertFalse(form.is_valid())
    
    def test_user_with_invalid_password_is_not_valid(self):
        form = UserForm(data={
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra!',
            'email' : 'email@gmail.com'
        })

        self.assertFalse(form.is_valid())

    def test_user_with_invalid_email_is_not_valid(self):
        form = UserForm(data={
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra1234567!',
            'email' : 'emailgmail.com'
        })

        self.assertFalse(form.is_valid())

    def test_edit_form_is_not_valid(self):
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())




class TestUrl(SimpleTestCase):
    
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_edit_url_is_resolved(self):
        url = reverse('user:editUser')
        self.assertEquals(resolve(url).func, editUser)

    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register = reverse('register')
        self.profile = reverse('profile')
        self.login = reverse('login')
        self.editUser = reverse('user:editUser')
    
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
        self.assertEquals(User.objects.count(), 1)
        
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

    def test_update_user(self):
        response = self.client.post(self.register, {
            'username' : 'Korisnik',
            'first_name' : 'OvoJeIme',
            'last_name' : 'OvoJePrezime',
            'password' : 'Sifra1234567!',
            'email' : 'email@gmail.com'
        })

        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(User.objects.get(username='Korisnik').username, 'Korisnik')

        login = self.client.login(username='Korisnik', password='Sifra1234567!')

        response = self.client.post(self.editUser, {
            'username' : 'NoviKorisnik'
        })

        self.assertEquals(User.objects.get(username='NoviKorisnik').username, 'NoviKorisnik')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 1)
    
   
    
    