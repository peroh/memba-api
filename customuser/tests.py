# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from customuser.models import CustomUser

# Create your tests here.

class UserCreationTest(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            "mperrott6@gmail.com",
            "matt",
            "perrott",
        )
    
    def tearDown(self):
        self.user.delete()
    
    def test_user_was_created(self):
        all_users = CustomUser.objects.all()
        self.assertIsNotNone(all_users)
        
    def test_user_email_is_correct(self):
        self.assertEqual("mperrott6@gmail.com", self.user.email)
        
    def test_user_first_name_is_correct(self):
        self.assertEqual("matt", self.user.first_name)

    def test_user_last_name_is_correct(self):
        self.assertEqual("perrott", self.user.last_name)
