from rest_framework import generics
from django.db.models import Q

from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        print query
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
            )
        return qs
