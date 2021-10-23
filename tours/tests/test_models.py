from django.test import TestCase
import tours.models as models 

class TestTourModels(TestCase):
    def test_TourCategory_str(self):
        title = models.TourCategory.objects.create(name="test category", order=1)
        self.assertEqual(str(title), "test category")

    def test_TourCategory_urlgen(self):
        object = models.TourCategory.objects.create(name="test1")
        self.assertEqual(f"/tours/category/{object.pk}", object.get_absolute_url())

