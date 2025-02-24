from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Mensajeria (TemplateView):
    template_name = 'mensajeria/mensajeria.html'