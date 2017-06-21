# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from customuser.models import CustomUser
from member.models import Member


class TestMemberList(APITestCase):
    def setUp(self):
        # Create users
        user1 = CustomUser.objects.create(
            email="abc@gmail.com", 
            first_name="Alan", 
            last_name="Turing"
        )
        user2 = CustomUser.objects.create(
            email="moffdaddy@gmail.com", 
            first_name="Alastair", 
            last_name="Moffat"
        )
        
        # Create members
        Member.objects.create(user=user1, dob="1940-05-01", nickname="Al")
        Member.objects.create(user=user2, dob="1960-06-03", nickname="The Moff")
        
        # Configure url
        self.url = reverse('member:list')
        
    def test_get_member_list(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)
        
    def test_member_email(self):
        member1 = Member.objects.get(pk=1)
        member2 = Member.objects.get(pk=2)
        self.assertEqual(member1.user.email, "abc@gmail.com")
        self.assertEqual(member2.user.email, "moffdaddy@gmail.com")
