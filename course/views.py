# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from course.serializers import CourseSerializer

from course.models import Course
from course.serializers import CourseSerializer

# List all Courses
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Create Course   
class CourseCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Add a members to a course
@api_view(['PATCH'])
def course_add_member(request, pk):
    attendees = request.data['attendees']
    course = Course.objects.get(pk=pk)
    if request.method == 'PATCH':
        for attendee in attendees:
            course.attendees.add(attendee)

    return Response({"message": "Success!"})
    
# Remove member from a course
# @api_view(['DELETE'])


# TODO 
# Remove members from a course
# Delete a course
# Update a course
