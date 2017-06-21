from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^award/', include('award.urls', namespace='award')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
