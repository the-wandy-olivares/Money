from django.views.generic import  TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render


class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"
