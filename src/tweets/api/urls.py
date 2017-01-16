from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    RetweetAPIView,
    LikeToggleAPIView,
)

urlpatterns = [
    url(r'^list-api/$', TweetListAPIView.as_view(), name="list-api"), #/api/tweet/
    url(r'^create-api/$', TweetCreateAPIView.as_view(), name="create-api"),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name="like-toggle"),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name="retweet"),
]
