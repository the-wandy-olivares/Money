from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy
from . import models 
from . import forms


class Inversion(TemplateView):
      template_name = "inversion/inversion.html"
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            inversions = models.Inversion.objects.filter(is_active=True).order_by('-pk').first()
            context['inversions'] = models.Inversion.objects.filter(is_active=True)
            if inversions:
                context['total_inversion'] = inversions.mount_inversion
                context['retorno_inversion'] = inversions.mount_retorno
            else:
                context['total_inversion'] = 0
                context['retorno_inversion'] = 0
            context['inversion_actual'] = inversions
            return context
      
      def get(self, request, *args, **kwargs):
            context = self.get_context_data(**kwargs)
            return render(request, self.template_name, context)


class InversionCreate(CreateView):
      template_name = "inversion/inversion-create.html"
      model = models.Inversion
      form_class = forms.Inversion
      
      def form_valid(self, form):
            form.instance.user = self.request.user
            form.instance.mount_disponible = form.instance.mount_inversion
            form.instance.company = self.request.user.more.company
            form.save()
            return super().form_valid(form)
      
      def form_invalid(self, form):
            print(form.errors)
            return super().form_invalid(form)
      
      def get_success_url(self):
            return reverse_lazy('inversion:inversion')



class InversionUpdate(UpdateView):
      template_name = "inversion/inversion-update.html"
      model = models.Inversion
      form_class = forms.Inversion
      
      def form_valid(self, form):
            form.instance.user = self.request.user
            form.instance.mount_disponible = form.instance.mount_inversion
            form.instance.company = self.request.user.more.company
            form.save()
            return super().form_valid(form)
      
      def form_invalid(self, form):
            print(form.errors)
            return super().form_invalid(form)
      
      def get_success_url(self):
            return reverse_lazy('inversion:inversion')


class InversionAgregarFondos(DetailView):
      model = models.Inversion
      template_name = 'inversion/inversion-agregar-fondos.html'
      context_object_name = 'inversion'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            inversion = self.get_object()
            context['inversion'] = inversion
            return context
      
      def post(self, request, *args, **kwargs):
            inversion = self.get_object()
            mount = request.POST.get('mount').replace(',', '')
            inversion.mount_inversion += int(mount)
            inversion.mount_disponible  += int(mount) 
            inversion.save()
            return redirect('inversion:inversion')
      
      def get_success_url(self):
            return reverse_lazy('inversion:inversion')