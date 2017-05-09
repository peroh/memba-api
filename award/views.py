# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from serializers import AwardSerializer

from award.models import Award

class AwardList(APIView):
    def get(self, request, format=None):
        awards = Award.objects.all()
        serializer = AwardSerializer(awards, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = AwardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Test(APIView):
    def get(self, request, format=None):
        print 'get request'
        
    def post(self, request, format=None):
        print 'post request'
