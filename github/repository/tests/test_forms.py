from django.test import TestCase
from repository.forms import RepositoryForm

class TestForms(TestCase):
    def test_repository_form_is_valid_no_members(self):
        form = RepositoryForm(data={
            'name' : 'Repo',
            'user' : ['Choose members']
        })

        self.assertTrue(form.is_valid())