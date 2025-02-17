
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView
from . import models
from .forms import CreditForm
from django.urls import reverse_lazy



class Credit(TemplateView):
    template_name = 'credit/credit.html'



class CreditCreate(CreateView):
    model = models.Credit
    form_class = CreditForm
    template_name = 'credit/credit-create.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('credit:credit-list')
    


class CreditUpdate(UpdateView):
      model = models.Credit
      form_class = CreditForm
      template_name = 'credit/credit-update.html'
      
      def form_valid(self, form):
            return super().form_valid(form)
      
      def get_success_url(self):
            return reverse_lazy('credit:credit-list')
      


class CreditDetail(DetailView):
      model = models.Credit
      template_name = 'credit/credit-detail.html'
      context_object_name = 'credit'



class CreditList(TemplateView):
      template_name = 'credit/credit-list.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['credits'] = models.Credit.objects.all()
            return context
      

class CreditDelete(DeleteView):
      model = models.Credit
      template_name = 'credit/credit-delete.html'
      
      def get_success_url(self):
            return reverse_lazy('credit:credit-list')