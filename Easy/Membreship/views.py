from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView 



class Membreship(TemplateView):
      template_name = "membreship/membreship.html"


