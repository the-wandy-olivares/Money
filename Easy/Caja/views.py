from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

class Caja (TemplateView):
      template_name = 'caja/caja.html'

      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            last_box = models.Box.objects.filter(open=False).latest('id')
            last_movimientos = models.Movements.objects.filter(box=last_box)
        except models.Box.DoesNotExist:
            last_movimientos = models.Movements.objects.none()

        try:
            box = models.Box.objects.get(open=True)
            movimientos = models.Movements.objects.filter(box=box)
        except models.Box.DoesNotExist:
            movimientos = models.Movements.objects.none()

        balance_apertura = 0
        ingresos = 0
        egresos = 0

        for movimiento in movimientos:
            if movimiento.type == 'ingreso':
                ingresos += movimiento.mount
            elif movimiento.type == 'gasto':
                egresos += movimiento.mount

        balance_caja = balance_apertura + ingresos - egresos
        total_ingresos = 0
        total_gastos = 0

        for movimiento in  models.Movements.objects.all():
            if movimiento.type == 'ingreso':
                total_ingresos += movimiento.mount
            elif movimiento.type == 'gasto':
                total_gastos += movimiento.mount

        last_ingreso = 0
        last_gasto = 0

        for movimiento in last_movimientos:
            if movimiento.type == 'ingreso':
                last_ingreso += movimiento.mount
            elif movimiento.type == 'gasto':
                last_gasto += movimiento.mount


        context['total_movimientos'] = total_ingresos - total_gastos

        context['total_last_session'] = last_ingreso - last_gasto

        context['is_open'] = models.Box.objects.filter(open=True).exists()
        context['movimientos'] = movimientos
        context['balance_apertura'] = balance_apertura
        context['ingresos'] = ingresos
        context['egresos'] = egresos
        context['balance_caja'] = balance_caja
        context['cajas'] = models.Box.objects.all()
        context['years'] = range(2025, 2028)  # Example range of years
        context['meses'] = [
                    {'numero': 1, 'nombre': 'Enero'},
                    {'numero': 2, 'nombre': 'Febrero'},
                    {'numero': 3, 'nombre': 'Marzo'},
                    {'numero': 4, 'nombre': 'Abril'},
                    {'numero': 5, 'nombre': 'Mayo'},
                    {'numero': 6, 'nombre': 'Junio'},
                    {'numero': 7, 'nombre': 'Julio'},
                    {'numero': 8, 'nombre': 'Agosto'},
                    {'numero': 9, 'nombre': 'Septiembre'},
                    {'numero': 10, 'nombre': 'Octubre'},
                    {'numero': 11, 'nombre': 'Noviembre'},
                    {'numero': 12, 'nombre': 'Diciembre'},
        ]
        return context

      def post(self, request, *args, **kwargs):
        tipo = request.POST.get('tipo')
        caja = request.POST.get('caja')
        year = request.POST.get('year')
        mes_inicio = request.POST.get('mes_inicio')
        mes_fin = request.POST.get('mes_fin')
        print(tipo)
        movimientos = models.Movements.objects.all()

        if tipo and tipo != 'todos':
            movimientos = movimientos.filter(type=tipo)

        if caja and caja != 'todas':
            movimientos = movimientos.filter(box=models.Box.objects.get(pk=int(caja)))

        if year and year != 'todos':
            movimientos = movimientos.filter(date__year=year)

        if mes_inicio and mes_inicio != 'todos':
            movimientos = movimientos.filter(date__month__gte=mes_inicio)

        if mes_fin and mes_fin != 'todos':
            movimientos = movimientos.filter(date__month__lte=mes_fin)

        balance_apertura = 0
        ingresos = 0
        egresos = 0

        for movimiento in movimientos:
            if movimiento.type == 'ingreso':
                ingresos += movimiento.mount
            elif movimiento.type == 'gasto':
                egresos += movimiento.mount

        balance_caja = balance_apertura + ingresos - egresos

        context = self.get_context_data()
        context['movimientos'] = movimientos
        context['balance_apertura'] = balance_apertura
        context['ingresos'] = ingresos
        context['egresos'] = egresos
        context['balance_caja'] = balance_caja

        return self.render_to_response(context)
    
