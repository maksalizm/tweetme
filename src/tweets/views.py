from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.forms.utils import ErrorList
from django import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


# Create your views here.

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    #
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj


class TweetListView(ListView):
    # queryset = Tweet.objects.all()
    template_name = "tweets/tweet_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['create_form'] = TweetModelForm
        context['create_url'] = reverse_lazy('tweet:create')
        print context
        return context


class TweetCreateView(FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    # fields = ['user', 'content']
    template_name = "tweets/tweet_create.html"
    # success_url = reverse_lazy('tweet:detail') #reverse
    #  login_url = "/tweet/"


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/tweet_update.html"
    # success_url = "/tweet/"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/tweet_delete_confirm.html"
    success_url = reverse_lazy('tweet:list')  # reverse_lazy
