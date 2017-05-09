from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    url(r'^$', views.MemberList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MemberDetail.as_view(), name='detail')
]