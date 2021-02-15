from django.test import SimpleTestCase
from django.urls import reverse, resolve
from github.views import register, profile
from user.views import editUser

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
    
    