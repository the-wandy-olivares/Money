from django.shortcuts import render
from django.views.generic import TemplateView


class Calculator(TemplateView):
      template_name = 'calculator/calculator.html'