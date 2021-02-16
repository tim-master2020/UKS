from django.test import SimpleTestCase
from django.urls import reverse, resolve
from label.views import all,addLabel,updateLabel,deleteLabel

class TestUrl(SimpleTestCase):
    def test_all_url_is_resolved(self):
        url = reverse('labels:all')
        self.assertEquals(resolve(url).func, all)

    def test_add_url_is_resolved(self):
        url = reverse('labels:addLabel',args=[1])
        self.assertEquals(resolve(url).func, addLabel)

    def test_update_url_is_resolved(self):
        url = reverse('labels:updateLabel', args=[1,1])
        self.assertEquals(resolve(url).func, updateLabel)

    def test_delete_url_is_resolved(self):
        url = reverse('labels:deleteLabel', args=[1,1])
        self.assertEquals(resolve(url).func, deleteLabel)