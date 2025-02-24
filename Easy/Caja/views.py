from django.shortcuts import render
from django.views.generic import TemplateView


class Caja (TemplateView):
      template_name = 'caja/caja.html'