from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from course import views

app_name = 'course'
urlpatterns = [
    url(r'^list$', views.CourseList.as_view(), name='list'),
    url(r'^create$', views.CourseCreate.as_view(), name='create'),
    url(r'^addmember/(?P<pk>[0-9]+)/$', views.course_add_member, 
        name='add-member'),
]