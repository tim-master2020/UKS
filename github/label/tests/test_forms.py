from django.test import TestCase
from label.forms import LabelForm


class TestForms(TestCase):
    def test_label_form_is_valid_add(self):
        form = LabelForm(data={
            'name' : 'bugfix',
            'color' : '#dcfae4'
        })

        self.assertTrue(form.is_valid())

    def test_repository_form_is_not_valid(self):
        form = LabelForm(data={
            'name' : '',
            'color' : '#dcfae4'
        })

        self.assertFalse(form.is_valid())