from django import setup
from django.test import TestCase
from tours.forms import TourCommentForm



class TestTourCommentForm(TestCase):
    def setUp(self) -> None:
        self.form = TourCommentForm
    
    def test_clean_email(self):
        form = self.form(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil.as',
            'comment': 'test'
        })
        form1 = self.form(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@as',
            'comment': 'test'
        })
        form2 = self.form(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        self.assertTrue(form.has_error('email'), "Email not validates @ symbol in mail")
        self.assertTrue(form1.has_error('email'), "Email not validates . symbol in mail")
        self.assertTrue(form1.has_error('email'), "Form has false errors with email field")

    def test_clean_name(self):
        form = self.form(data={
            'full_name': 'Kamil@Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        form1 = self.form(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        self.assertFalse(form.has_error('full_name'), "Name lets @ symbol to be in name")
        self.assertFalse(form1.has_error('full_name'), "Form has false errors with name field")
