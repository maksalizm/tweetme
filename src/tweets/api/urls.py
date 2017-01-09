from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    # TweetDetailView,
    # TweetListView,
    # TweetCreateView,
    # TweetUpdateView,
    # TweetDeleteView
)

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^list-api/$', TweetListAPIView.as_view(), name="list-api"), #/api/tweet/
    url(r'^create-api/$', TweetCreateAPIView.as_view(), name="create-api"),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),
]
