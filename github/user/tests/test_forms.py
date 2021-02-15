from django.test import TestCase
from user.forms import UserForm, UserUpdateForm

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

    def test_edit_form_is_not_valid(self):
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())