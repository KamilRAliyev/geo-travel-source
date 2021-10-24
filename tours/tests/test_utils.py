from django.test import TestCase
import tours.utils as utils
from tours import models

class TestUtils(TestCase):
    def setUp(self) -> None:
        self.category = models.TourCategory.objects.create(name="test_category", order=1)
        self.tour = models.Tour.objects.create(name="tour1", description="none", price=19.99, duration=5, city="Baku", category=self.category)

    def test_random_string_gen(self):
        randstrgen = utils.random_string_generator
        lst = []
        lst_unique = []
        for i in range(1000):
            value = randstrgen()
            lst.append(value)
            if value not in lst_unique:
                lst_unique.append(value)
        
        self.assertTrue(lst == lst_unique, msg="Random string generator not generates unique values")

    def test_unique_slug_generator(self):
        unslgen = utils.unique_slug_generator
        lst = []
        lst_unique = []
        for i in range(1000):
            value = unslgen(instance=self.tour)
            lst.append(value)
            if value not in lst_unique:
                lst_unique.append(value)
        
        self.assertTrue(lst == lst_unique, msg="Unique slug generator not generates unique values")
