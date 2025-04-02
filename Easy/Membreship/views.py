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
                        "Calculadora de intereses", 
                        "Gestion de creditos",
                        "Flujo de caja",
                        "Modulo de clientes",
                        "Notificaciones avanzadas, alertas, avisos.",
                        "Facturas automaticas","Envio por correo de facturas redactada por (IA)",
                        "Notificaciones",
                        "Geolocaliaciones de clientes, proveedores y mas",
                        "Buro de crédito", 
                        "Integracion de mensajeria, WhatsApp, Facebook, Instagram, Telegram"
                        "Propio dominio",
                        "Control de inversión",
                        "Agente inteligente (IA)",
                        "Reportes fiscales",
                        "Contratos digitales",
                        "Disponibilidad de mensajeros",
                        "Avances de créditos de hasta $1,000 dolares"
                  ]
            return context
   
      def get(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                  return redirect('login:login')  # Cambia 'login' por el nombre de tu URL
            return super().get(request, *args, **kwargs)
      

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