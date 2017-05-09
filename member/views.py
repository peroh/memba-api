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
    

class MemberUserList(generics.GenericAPIView):
    def get(self, request):
        members = Member.objects.all()
        users = CustomUser.objects.all()
        
        context = {
            "request": request,
        }
        
        member_serializer = MemberSerializer(members, many=True, context=context)
        user_serializer = CustomUserSerializer(users, many=True, context=context)
        
        return Response(response)
        