from django import setup
from django.core.exceptions import ValidationError
from django.test import TestCase
from tours.forms import TourCommentForm
from django import forms



class TestTourCommentForm(TestCase):
   
    def test_clean_email(self):
        form = TourCommentForm(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil.as',
            'comment': 'test'
        })
        form1 = TourCommentForm(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@as',
            'comment': 'test'
        })
        form2 = TourCommentForm(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        self.assertTrue(form.has_error('email'), "Email not validates @ symbol in mail")
        self.assertTrue(form1.has_error('email'), "Email not validates . symbol in mail")
        self.assertTrue(form1.has_error('email'), "Form has false errors with email field")

    def test_clean_name(self):
        formm = TourCommentForm(data={
            'full_name': 'Kamil@Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        formm1 = TourCommentForm(data={
            'full_name': 'Kamil Aliyev',
            'email': 'kamil@gmail.com',
            'comment': 'test'
        })
        self.assertFalse(formm.has_error('full_name'), "Name lets @ symbol to be in name")
        self.assertFalse(formm1.has_error('full_name'), "Form has false errors with name field")
