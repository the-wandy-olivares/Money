from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView 

from .models import Plans, Carateristica

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
            # self.AdminiCaracteristicas(servicios, 'Recomendado', False, True)˝
            return context
      

      def AdminiCaracteristicas(self, servicios=list, name_plan='', delete_carateristic=False, is_active_carateristica=True):
            #  Crear caracteristicas
            plan_select = Plans.objects.get(is_active=True, name=name_plan)
            if delete_carateristic == False:
                  lista = servicios
                  for element in lista:
                        if not Carateristica.objects.filter(plan=plan_select, name=element).exists():
                              Carateristica.objects.create( plan=plan_select, name=element, is_active= is_active_carateristica )
                        finished = f'Se crearon correctamente: {Carateristica.objects.filter(plan=plan_select, name=element).count()}  caracteristicas del plan {plan_select.name} ' 
                        print(finished)
                  return finished
            else:
                  # Eliminar caracteristicas
                  ctr = Carateristica.objects.filter(plan=plan_select)
                  for c in ctr:
                        c.delete()
            return f'Se eliminaron correctamente todas las caracteristicas'