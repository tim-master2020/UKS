from django.test import SimpleTestCase
from django.urls import reverse, resolve
from repository.views import allRepositories, addRepository, delete_view, update_view, detail_view

class TestUrl(SimpleTestCase):
    def test_all_url_is_resolved(self):
        url = reverse('repository:allRepositories')
        self.assertEquals(resolve(url).func, allRepositories)

    def test_add_url_is_resolved(self):
        url = reverse('repository:addRepository')
        self.assertEquals(resolve(url).func, addRepository)

    def test_delete_url_is_resolved(self):
        url = reverse('repository:deleteRepository', args=[1])
        self.assertEquals(resolve(url).func, delete_view)