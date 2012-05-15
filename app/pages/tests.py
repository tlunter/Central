from django.test import TestCase
from django.test.client import Client
from app.functions import full_title

class MainPageTest(TestCase):
    
    def test_has_title_index(self):
        response = self.client.get('/')
        
        self.assertContains(response, full_title('Index'))
        