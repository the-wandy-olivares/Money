from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView


class Client(TemplateView):
    template_name = 'client/client.html'