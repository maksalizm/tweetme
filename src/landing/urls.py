from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$/', Landing.as_view(), name="Landing"),
]