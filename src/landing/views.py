from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.http import JsonResponse


# Create your views here.

class Landing(TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print request.POST
            return JsonResponse({"success": "True"})

