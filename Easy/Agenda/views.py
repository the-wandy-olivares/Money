from django.shortcuts import render
from django.views.generic import TemplateView


class Agenda (TemplateView):
      template_name = 'agenda/agenda.html'