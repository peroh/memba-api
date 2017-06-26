from django.urls import reverse
from rest_framework.test import APITestCase

from award.models import AwardCategory
from customuser.models import CustomUser
from member.models import Member
from course.models import Course

class TestCourseList(APITestCase):
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
        # Assign members to course
        self.course1.attendees.add(self.member1, self.member2)
        
        self.course2 = Course.objects.create(
            title = "Course2",
            award_category = category2,
        )
        
        # Configure url
        self.url = reverse('course:list')
        

    def test_get_course_list(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)
        
    def test_course_member_name(self):
        member1_name = self.course1.attendees.get(pk=1).user.first_name
        self.assertEqual(member1_name, "Alan")

        
        
    