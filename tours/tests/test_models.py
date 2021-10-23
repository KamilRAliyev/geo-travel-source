from django.test import TestCase
from tours.models import get_filename_ext, upload_image_path
import tours.models as models 
from tours import utils
from tours.views import tour_comment

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
    
    def test_TourOrders_str(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        tour_order = models.TourOrders(tour_name=tour.name, full_name="test persona", email='test@mail.com', price=tour.price)
        self.assertEqual(str(tour_order), f"Tour: {tour_order.tour_name}, Person: {tour_order.full_name}, Order date: {tour_order.order_date}")

    def test_TourSlider_str(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        tour_slider = models.TourSliderImages.objects.create(tour=tour)
        self.assertEqual(str(tour_slider), f"Tour: {str(tour)}, Image None")

    def test_TourComments_str(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        tour_comment = models.TourComments(full_name="test persona", email="test@mail.com", comment="Test comment", tour=tour)
        self.assertEqual(str(tour_comment), f"Name: {tour_comment.full_name}, Comment {tour_comment.comment[:100]}")

    def test_TourPriceTable_str(self):
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour = models.Tour.objects.create(name="tour1", description="none", price=9.99, duration=5, city="Baku", category=category)
        tpt = models.TourPriceTable.objects.create(tour=tour,price=19.99,desc="")
        self.assertEqual(str(tpt), f"{tour.name} | Price: {tpt.price} Desc: {tpt.desc}")

class TestUtilizedFunctions(TestCase):
    def test_get_filename_ext(self):
        path=""
        
        self.assertEqual(get_filename_ext(path), ("",""), "Function: get_filename_ext edge case error. Function cannot handle empty string.")
        path="test/adil.jpg"
        self.assertEqual(get_filename_ext(path), ('test','adil.jpg'), "Function: get_filename_ext error. Function cannot split normal filename and its extension.")
        path="/home/kamil/Documents/Certificates/test.pdf"
        self.assertEqual(get_filename_ext(path), ("/home/kamil/Documents/Certificates","test.pdf"), "Function: get_filename_ext not works properly.")

    def test_upload_path(self):
        path="test/adil.jpg"
        self.assertEqual(upload_image_path(instance="",filename=path), 'tours/test/testadil.jpg')
