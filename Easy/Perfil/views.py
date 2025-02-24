from django.shortcuts import render
from django.views.generic import TemplateView

class Perfil(TemplateView):
      template_name = 'perfil/perfil.html'