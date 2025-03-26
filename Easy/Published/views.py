from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Published (TemplateView):
    template_name = 'published/published.html'