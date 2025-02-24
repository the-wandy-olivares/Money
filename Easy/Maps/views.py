from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Maps (TemplateView):
    template_name = 'maps/maps.html'