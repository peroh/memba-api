# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.response import Response
from customuser.serializers import CustomUserSerializer
from member.serializers import MemberSerializer
from customuser.models import CustomUser
from member.models import Member


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer