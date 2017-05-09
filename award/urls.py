from django.conf.urls import url

from award import views

urlpatterns = [
    url(r'^$', views.AwardList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',  views.AwardDetail.as_view()),
]