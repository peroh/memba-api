from django.conf.urls import url

from award import views

app_name = 'award'
urlpatterns = [
    url(r'^$', views.AwardList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$',  views.AwardDetail.as_view(), name='detail'),
]