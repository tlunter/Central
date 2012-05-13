from django.test.client import Client
from django.test import TestCase
from django.db import IntegrityError
from app.accounts.models import User

class AccountTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username = 'Test Name', password = 'testpass', email = 'test@example.com')
        
    def test_duplicate_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(username = 'Test Name', password = 'testpass', email = 'testing@example.com')
            
    def test_duplicate_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(username = 'Test 2 Other Name', password = 'testpass', email = 'test@example.com')
            
class AccountProfilePage(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.username = 'NameOnPage'
        cls.password = 'testpass'
        cls.user = User.objects.create_user(username = cls.username, password = cls.password, email = 'nameonpage@example.com')
    
    def setUp(self):
        self.client = Client()
        
    def test_username(self):
        response = self.client.get('/profile/NameOnPage/')
        
        self.assertContains(response, 'NameOnPage')
        
    def test_no_username(self):
        self.client.login(username = self.username, password = self.password)
        response = self.client.get('/profile/')
        
        self.assertContains(response, self.username)