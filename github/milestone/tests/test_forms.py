from django.test import SimpleTestCase
from milestone.forms import MilestoneForm

class TestForms(SimpleTestCase):

    def test_milestone_valid_data_form(self):
        form = MilestoneForm(data={
            'title' : 'UKS',
            'description' : 'first description',
            'dueDate' : '02/14/21'
        })

        self.assertTrue(form.is_valid())

    def test_milestone_invalid_data_form(self):
        form = MilestoneForm(data={
            'title' : 'UKS',
            'description' : 'first description',
            'dueDate' : 'date'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_milestone_no_data_form(self):
        form = MilestoneForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)