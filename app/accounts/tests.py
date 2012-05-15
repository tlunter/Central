from django.db import IntegrityError
from django.test import TestCase
from django.test.client import Client
from django.utils.html import escape
from app.functions import full_title
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
        cls.otheruser = User.objects.create_user(username = 'Other', password = 'other', email = 'other@example.com')

    def setUp(self):
        self.client.login(username = self.username, password = self.password)
        
    def test_username(self):
        response = self.client.get('/profile/Other/')
        
        self.assertContains(response, 'Other')
        
    def test_no_username(self):
        response = self.client.get('/profile/')
        
        self.assertContains(response, self.username)
        
    def test_has_title_profile(self):
        response = self.client.get('/profile/Other/')
        
        self.assertContains(response, '<title>{0}</title>'.format(escape(full_title('Other\'s Profile'))))
        
    def test_has_title_your_profile(self):
        response = self.client.get('/profile/')
        
        self.assertContains(response, '<title>{0}</title>'.format(full_title('Your Profile')))
        
    def test_has_h1_profile(self):
        response = self.client.get('/profile/Other/')
        
        self.assertContains(response, '<h1>{0}</h1>'.format(escape('Other\'s Profile')))
        
    def test_has_h1_your_profile(self):
        response = self.client.get('/profile/')
        
        self.assertContains(response, '<h1>{0}</h1>'.format(escape('Your Profile')))