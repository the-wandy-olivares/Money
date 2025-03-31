from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, RedirectView
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
from .models import Plans, Carateristica, Payment
import uuid #Para pruebas 
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.shortcuts import render, redirect


class Membreship(TemplateView):
      template_name = "membreship/membreship.html"


      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['plans'] =  Plans.objects.filter(is_active=True)
            servicios = [
                  "Asesoria financiera básica",
                  "Calculadora de intereses",
                  "Clientes",
                  "Herramientas de presupuesto",
                  "1 cuenta de inversión",
                  "Reportes en PDF y Excel",
                  "Contratos digitales",
                  "Mensajeros (minimo de DO$100)",
                  "Creación de eventos",
                  "Ubicación de clientes en un mapa",
                  "Notificaciones avanzadas y alertas",
                  "Maps", "Creditos", "Flujo de caja",
                  "Buro de crédito",
                  "Dominio propio",
                  "Asistencia personalizada",
                  "Avances de créditos de hasta $5,000 dolares"
                  ]
            # self.AdminiCaracteristicas(servicios, 'Recomendado', False, True)
            return context
      
      def get(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                  return redirect('login:login')  # Cambia 'login' por el nombre de tu URL
            return super().get(request, *args, **kwargs)

      # def AdminiCaracteristicas(self, servicios=list, name_plan='', delete_carateristic=False, is_active_carateristica=True):
      #       #  Crear caracteristicas
      #       plan_select = Plans.objects.get(is_active=True, name=name_plan)
      #       if delete_carateristic == False:
      #             lista = servicios
      #             for element in lista:
      #                   if not Carateristica.objects.filter(plan=plan_select, name=element).exists():
      #                         Carateristica.objects.create( plan=plan_select, name=element, is_active= is_active_carateristica )
      #                   finished = f'Se crearon correctamente: {Carateristica.objects.filter(plan=plan_select, name=element).count()}  caracteristicas del plan {plan_select.name} ' 
      #                   print(finished)
      #             return finished
      #       else:
      #             # Eliminar caracteristicas
      #             ctr = Carateristica.objects.filter(plan=plan_select)
      #             for c in ctr:
      #                   c.delete()
      #       return f'Se eliminaron correctamente todas las caracteristicas'
      

class PaymentPaypal(TemplateView):
      template_name = "membreship/paypal/payment-paypal.html"
      def get(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                  return redirect('login:login')  # Cambia 'login' por el nombre de tu URL
            return super().get(request, *args, **kwargs)
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            plan = Plans.objects.get(id=self.kwargs.get('pk'))
            paypal_dict = {
                  'business': settings.PAYPAL_RECEIVER_EMAIL,
                  'amount':  f"{plan.price:,.2f}",  # Monto en USD o moneda 
                  'item_name': plan.name,
                  'currency_code': 'USD',
                  'invoice': f"INV-{uuid.uuid4().hex[:12].upper()}-{self.request.user.id}",
                  'notify_url': self.request.build_absolute_uri('/paypal/'),
                  'return_url': self.request.build_absolute_uri(reverse('membreship:payment-done')),
                  'cancel_return': self.request.build_absolute_uri(reverse('membreship:payment-canceled')),
            }

            form = PayPalPaymentsForm(initial=paypal_dict)
            context['form'] = form
            context['id_plan'] = plan.id
            context['id_user'] = self.request.user.id
            return context
      
      def post(self, request, *args, **kwargs):
            form = PayPalPaymentsForm()
            if form.is_valid():
                  return render(request, 'membreship/paypal/payment-paypal.html', {'form': form})
            else:
                  return render(request, 'membreship/paypal/payment-error.html', {'error': 'Error en el formulario de PayPal'})
      

class PaypalDone(TemplateView):
      template_name = "membreship/paypal/paypal-done.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context

class PaypalDone(TemplateView):
      template_name = "membreship/paypal/paypal-done.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
      
class PaypalCaceled(TemplateView):
      template_name = "membreship/paypal/paypal-canceled.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context