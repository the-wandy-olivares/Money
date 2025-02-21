
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView
from . import models
from .forms import CreditForm
from django.urls import reverse_lazy
from .mixing import  Calculadora_Intereses, Calculadora_Moras 
from django.utils import timezone
import json


class Credit(TemplateView):
    template_name = 'credit/credit.html'



class CreditCreate(CreateView):
    model = models.Credit
    form_class = CreditForm
    template_name = 'credit/credit-create.html'

    def form_valid(self, form):
      form.instance.start_date =  timezone.now()
      credit = form.save(commit=False)
      Calculadora_Intereses(form.instance.capital, form.instance.
      cuotas, form.instance.intereses, credit)
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

      def get(self, request, *args, **kwargs):
            self.object = self.get_object()
            # Calculadora_Moras(self.object)
            return self.render_to_response(self.get_context_data(object=self.object))

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            self.object = self.get_object()
            Calculadora_Moras(self.object)
            context['cuotas'] = models.Cuotas.objects.filter(credit=self.object)
            return context
      

      def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            lista_cuotas = request.POST.get('lista_cuotas')

            cleaned_pay = request.POST.get('payment').replace(',', '')
            payment = int(cleaned_pay)

      
            if lista_cuotas and payment:
                  lista_cuotas = json.loads(lista_cuotas)
                  for id_cuota in lista_cuotas:
                        cuota = models.Cuotas.objects.get(id=int(id_cuota))
                        if payment != 0: # Si el pago es diferente de 0, se procede a realizar el pago
                              if cuota.monto_mas_mora <= payment:
                                    payment -= cuota.monto_mas_mora
                                    print(payment)
                                    cuota.monto_mas_mora = 0
                                    cuota.payment = True

                              else:
                                    # Si el pago es menor al monto de la cuota, se procede a realizar el abono, empezando por la mora
                                    cuota.abono += payment
                                    cuota.monto_mas_mora -= cuota.abono # Se abona al monto
                                    payment -= cuota.abono
                                    if cuota.mora != 0:
                                          cuota.mora -= cuota.abono
                                    # cuota.mora -= payment
                                    else: # Si no hay mora, se abona al monto
                                          cuota.monto_mas_mora -= payment
                        cuota.save()
                        print(cuota.payment)

            
            return self.get(request, *args, **kwargs)



class CreditList(TemplateView):
      template_name = 'credit/credit-list.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['credits'] = models.Credit.objects.all()
            return context
      

class CreditDelete(DeleteView):
      model = models.Credit
      template_name = 'credit/credit-delete.html'
      context_object_name = 'credit'
      
      def get_success_url(self):
            return reverse_lazy('credit:credit-list')