from django.test import TestCase
from geotravel_app.models import AboutUs
import tours.models as models
from time import sleep

# User should be able to see new tours first
# User shoul be able to filters tours by city and by price
class TestTourListView(TestCase):
    def setUp(self) -> None:
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour1 = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        sleep(3)
        tour2 = models.Tour.objects.create(name="tour2", description="none", price=9.99, duration=5, city="Baku", category=category)
        about = AboutUs.objects.create(name='1',content='')
    def test_new_tours_first(self):
        response = self.client.get('tours/')

        queryset = models.Tour.objects.all().order_by('created_at').reverse()[:5]
        response_tours = response.context['tours']

        self.assertEqual(response.status_code, 200, "Tour List View not working.")
        self.assertEqual(queryset, response_tours)