from django.views.generic import  TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from Client import models


class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cont_clients'] = models.Client.objects.all().count()
        return context
