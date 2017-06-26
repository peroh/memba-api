from django.test import TestCase

from customuser.tests.factories import CustomUserFactory

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUserFactory.create()
        
    def test_get_full_name(self):
        full_name = self.user.get_full_name()
        self.assertEqual(full_name, self.user.email)
        
    def test_get_first_name(self):
        first_name = self.user.get_first_name()
        self.assertEqual(first_name, self.user.first_name)
    
    def test_get_last_name(self):
        last_name = self.user.get_last_name()
        self.assertEqual(last_name, self.user.last_name)
