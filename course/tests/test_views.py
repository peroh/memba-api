from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from award.models import AwardCategory
from customuser.models import CustomUser
from member.models import Member
from course.models import Course


class TestCourseAddMember(APITestCase):
    
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
        self.member1 = Member.objects.create(
            user=user1, 
            dob="1940-05-01", 
            nickname="Al"
        )
        self.member2 = Member.objects.create(
            user=user2, 
            dob="1960-06-03", 
            nickname="The Moff"
        )
        
        # Create some courses
        self.course1 = Course.objects.create(
            title = "Course1",
            award_category = category1,
        )
        
        self.course2 = Course.objects.create(
            title = "Course2",
            award_category = category2,
        )
        
        self.url = reverse('course:add-member', args=[1,])
        self.pk = 1
        self.data = {'attendees': [self.pk]}
        
    def test_course_add_member(self):
        self.client.patch(self.url, self.data, format='json')
        actual = self.course1.attendees.get(pk=self.pk).nickname
        expected = "Al"
        self.assertEqual(actual, expected)
    
    
class TestCourseAdd(APITestCase):
    
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
        
        self.url = reverse('course:create')
        self.data = {
                        'title': 'Badass Bronze Course',
                        'award_category': 1,
                     }
    
    def test_add_course(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('title'), self.data.get('title'))
        self.assertEqual(response.data.get('award_category'), 
                         self.data.get('award_category'))
        
        
        
        
        
        
        
        
        
        
        
        
            