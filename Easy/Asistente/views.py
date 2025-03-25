from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import requests


class Asistente(TemplateView):
    template_name = 'asistente/asistente.html'
