from django.urls import reverse
from rest_framework.test import APITestCase

from award.models import Award, AwardCategory
from customuser.models import CustomUser
from member.models import Member
from course.models import Course

class TestAwardList(APITestCase):
    def setUp(self):
        # Create some award categories
        category1 = AwardCategory.objects.create(
            title="Bronze", 
            description="Bronze Medallion"
        )
        category2 = AwardCategory.objects.create(
            title="SRC",
            description="Surf Rescue Certificate"
        )
                                                 
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
        member1 = Member.objects.create(
            user=user1, 
            dob="1940-05-01", 
            nickname="Al"
        )
        member2 = Member.objects.create(
            user=user2, 
            dob="1960-06-03", 
            nickname="The Moff"
        )

        # Create some awards
        award1 = Award.objects.create(
            award_category=category1,
            member=member1,
            attained="2017-06-01"
        )
        award2 = Award.objects.create(
            award_category=category2,
            member=member2,
            attained="2017-06-02"
        )
        award3 = Award.objects.create(
            award_category=category1,
            member=member2,
            attained="2017-06-03"
        )
        
        # Create some courses
        course1 = Course.objects.create(
            award_category=category1
        )
        course2 = Course.objects.create(
            award_category=category2
        )
        course3 = Course.objects.create(
            award_category=category1
        )
        
        # Configure url
        self.url = reverse('award:list')
        
    def test_get_award_list(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 3)
        