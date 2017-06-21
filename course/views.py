# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
# from course.serializers import CourseSerializer

from course.models import Course
from course.serializers import CourseSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
