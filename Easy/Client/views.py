from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView
from .models import Client

class Client(TemplateView):
    template_name = 'client/client.html'


class ClientList(TemplateView):
    template_name = 'client/client-list.html'
