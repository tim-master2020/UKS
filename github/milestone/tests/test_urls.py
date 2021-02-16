from django.test import SimpleTestCase
from django.urls import reverse, resolve
from milestone.views import all_milestones, add_milestone, update_milestone, delete_milestone

class TestUrls(SimpleTestCase):

    def test_all_url_is_resolved(self):
        url = reverse('milestone:allMilestones')
        self.assertEquals(resolve(url).func, all_milestones)

    def test_add_url_is_resolved(self):
        url = reverse('milestone:addMilestone', args=[1])
        self.assertEquals(resolve(url).func, add_milestone)

    def test_update_url_is_resolved(self):
        url = reverse('milestone:updateMilestone', args=[1,2])
        self.assertEquals(resolve(url).func, update_milestone)

    def test_delete_url_is_resolved(self):
        url = reverse('milestone:deleteMilestone', args=[1,2])
        self.assertEquals(resolve(url).func, delete_milestone)