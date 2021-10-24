from django.test import TestCase, RequestFactory
from geotravel_app.models import AboutUs
import tours.models as models
from time import sleep
from http import HTTPStatus

# User should be able to see new tours first
# User shoul be able to filters tours by city and by price
class TestTourListView(TestCase):
    def setUp(self) -> None:
        category = models.TourCategory.objects.create(name="test_category", order=1)
        tour1 = models.Tour.objects.create(name="tour1", description="none", price=19.99, duration=5, city="Baku", category=category)
        sleep(3)
        tour2 = models.Tour.objects.create(name="tour2", description="none", price=59.99, duration=5, city="Quba", category=category)
        self.path = '/tours/'

    def test_new_tours_first(self):
        response = self.client.get(path=self.path)

        queryset = models.Tour.objects.all().order_by('created_at').reverse()
        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]
       
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response_tours), 2)
        self.assertTrue(queryset,tour_lst)

    def test_filter_by_city(self):
        response = self.client.post(path=self.path, data={
            'city': "Baku"
        })
        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]

        queryset = models.Tour.objects.all().order_by('created_at').reverse()
        query = [model  for model in queryset if model.city=='Baku' ]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response_tours), 1)
        self.assertTrue(query,tour_lst)

    def test_filter_by_price(self):
        response = self.client.post(path=self.path, data={
            'amount': "$19",
            'amount2': "$21"
        })
        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]

        queryset = models.Tour.objects.all().order_by('created_at').reverse()
        query = [model  for model in queryset if model.price < 21.00 and model.price > 19.00  ]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response_tours), 1)
        self.assertTrue(query,tour_lst)


class TestTourCategoryView(TestCase):
    def setUp(self) -> None:
        self.category1 = models.TourCategory.objects.create(name="test_category1", order=1)
        self.tour1 = models.Tour.objects.create(name="tour1", description="none", price=19.99, duration=5, city="Baku", category=self.category1)
        sleep(3)
        self.category2 = models.TourCategory.objects.create(name="test_category2", order=2)
        self.tour2 = models.Tour.objects.create(name="tour2", description="none", price=59.99, duration=5, city="Quba", category=self.category2)
        sleep(3)
        self.tour3 = models.Tour.objects.create(name="tour3", description="none", price=109.99, duration=5, city="Fuzuli", category=self.category2)
        self.path = '/tours/category/'

    def test_new_tours_first(self):
        response = self.client.get(path=f"{self.path}{self.category2.pk}")
        queryset = models.Tour.objects.all().filter(category=self.category2.pk).order_by('created_at').reverse()

        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]
       
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response_tours), 2)
        self.assertTrue(queryset,tour_lst)

    def test_filter_by_city(self):
        response = self.client.post(path=f"{self.path}{self.category2.pk}", data={
            'city': "Baku"
        })
        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]

        queryset = models.Tour.objects.all().filter(category=self.category2.pk).order_by('created_at').reverse()
        query = [model  for model in queryset if model.city=='Baku' ]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(query,tour_lst)

    def test_filter_by_price(self):
        response = self.client.post(path=f"{self.path}{self.category2.pk}", data={
            'amount': "$57",
            'amount2': "$120"
        })
        response_tours = response.context['tours']
        tour_lst = [a for a in response_tours ]

        queryset = models.Tour.objects.all().order_by('created_at').reverse()
        query = [model  for model in queryset if model.price < 121.00 and model.price > 57.00  ]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(response_tours), 2)
        self.assertTrue(query,tour_lst)

class TestTourDetails(TestCase):
    def setUp(self) -> None:
        self.category = models.TourCategory.objects.create(name="test_category1", order=1)
        self.tour1 = models.Tour.objects.create(name="tour1", description="none", price=19.99, duration=5, city="Baku", category=self.category)
        self.tour_price_table = models.TourPriceTable.objects.create(tour=self.tour1, price=self.tour1.price, desc="Test Price") 
        self.path = f"/tours/tour/{self.tour1.slug}"
    
    def test_tour_get(self):
        response = self.client.get(self.path)
        test_tour = self.tour1
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['tour'], test_tour)

    def test_tour_order(self):
        response = self.client.post(path=self.path, data={
            'full_name': 'Kamil Aliyev',
            'email': 'test@mail.com',
            'select': '1',
        })
        
        self.assertEqual(response.context['message'], "We got your message. We will contact you by test@mail.com, in the shortest period.")

class TestTourComment(TestCase):
    def setUp(self) -> None:
        self.category = models.TourCategory.objects.create(name="test_category1", order=1)
        self.tour1 = models.Tour.objects.create(name="tour1", description="none", price=19.99, duration=5, city="Baku", category=self.category)
        self.tour_price_table = models.TourPriceTable.objects.create(tour=self.tour1, price=self.tour1.price, desc="Test Price") 
        self.path = f"/tours/tour/{self.tour1.slug}/comment"
    
    def test_tour_commenting(self):
        response = self.client.post(path=self.path, data={
            "full_name": "Kamil Aliyev",
            "email": "test@mail.com",
            "comment": "test comment" 
        })
        
        tour_comments = models.TourComments.objects.filter(tour=self.tour1.pk)
        tour_comment_list = [i.comment for i in tour_comments]
        
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/tours/tour/{self.tour1.slug}")
        self.assertIn('test comment', tour_comment_list)