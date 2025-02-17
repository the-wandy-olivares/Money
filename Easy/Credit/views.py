
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView
from . import models
from django.urls import reverse_lazy

class Credit(TemplateView):
    template_name = 'credit/credit.html'

