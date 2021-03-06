from django.test import TestCase
from repository.forms import RepositoryForm

class TestForms(TestCase):
    def test_repository_form_is_valid_no_members(self):
        form = RepositoryForm(data={
            'name' : 'Repo',
            'user' : ['Choose members']
        })

        self.assertTrue(form.is_valid())

    def test_repository_form_is_valid_with_members(self):
        form = RepositoryForm(data={
            'name' : 'Repo',
            'user' : ['mina']
        })

        self.assertTrue(form.is_valid())

    def test_repository_form_is_not_valid(self):
        form = RepositoryForm(data={})

        self.assertFalse(form.is_valid())