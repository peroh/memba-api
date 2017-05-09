# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from serializers import AwardSerializer

from award.models import Award


class AwardList(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
