from django.test import TestCase
import tours.models as models 
from . import utils

class TestTourModels(TestCase):
    def test_TourCategory_str(self):
        title = models.TourCategory.objects.create(name="test category", order=1)
        self.assertEqual(str(title), "test category")

    def test_TourCategory_urlgen(self):
        object = models.TourCategory.objects.create(name="test1")
        self.assertEqual(f"/tours/category/{object.pk}", object.get_absolute_url())

    def test_Tour_str(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)

        self.assertEqual(str(tour), f"{tour.name} | {tour.description}")
    
    def test_Tour_urlgen(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        self.assertEqual(f'/tours/tour/{tour.slug}', tour.get_absolute_url())
    
