from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.forms.utils import ErrorList
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin

# Create your views here.

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    #
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        print context
        return context


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    # fields = ['user', 'content']
    template_name = "tweets/form.html"
    success_url = "/tweet/create/"
    # login_url = "/admin/"
    #

