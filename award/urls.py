from django.conf.urls import url

from award import views

urlpatterns = [
    url(r'^$', views.AwardList.as_view()),
]