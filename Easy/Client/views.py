from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView
from . import models
from .forms import ClientForm
from django.urls import reverse_lazy

class Client(TemplateView):
    template_name = 'client/client.html'


class ClientCreate(CreateView):
    model = models.Client
    form_class = ClientForm
    template_name = 'client/client-create.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('client:client-list')


class ClientUpdate(UpdateView):
    model = models.Client
    form_class = ClientForm
    template_name = 'client/client-update.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('client:client-list')

class ClientDetail(DetailView):
    model = models.Client
    template_name = 'client/client-detail.html'
    context_object_name = 'client'


class ClientList(TemplateView):
    template_name = 'client/client-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = models.Client.objects.all()
        return context
    


class ClientDelete(DeleteView):
    model = models.Client
    template_name = 'client/client-delete.html'

    def get_success_url(self):
        return reverse_lazy('client:client-list')