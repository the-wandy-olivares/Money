from dateutil.relativedelta import relativedelta
from calendar import monthrange
from datetime import datetime, timedelta
import calendar

from . import models

class Opciones:
      FRECUENCIA = [ 
            ('mensual', 'Mensuales '), ('semanal', 'Semanales' ), ('quincenal', 'Quincenales')
      ]

      METODO = [ ('frances', 'Frances'), ( 'americano', 'Americano') ]



        
def Calculadora_Intereses( capital_, cuotas_, tasa_, credit):
      capital = int(capital_.replace(',', ''))
      cuotas = cuotas_
      tasa = int(tasa_) / 100
      cuota = capital * tasa / (1 - (1 + tasa) ** -cuotas)
      saldo = capital
      start_date = credit.start_date

      for mes in range(1, cuotas + 1):
            interes = saldo * tasa
            amortizacion_capital = cuota - interes
            saldo -= amortizacion_capital

            # Ajusta el día al valor de day_pay para start_date
            last_day_of_month = monthrange(start_date.year, start_date.month)[1]
            if credit.day_pay > last_day_of_month:
                  start_date = start_date.replace(day=last_day_of_month)
            else:
                  start_date = start_date.replace(day=credit.day_pay)
            
            if not credit.pk:
                  credit.save()
            count_cuotas = models.Cuotas(
                  credit=credit, monto=round(cuota, 2), monto_mas_mora=round(cuota, 2),
                  start_date=datetime.now() + relativedelta(months=mes-1), 
                  end_date=(datetime.now() + relativedelta(months=mes-1)) + timedelta(days=5)
            )
            count_cuotas.save()

            # Incrementar el mes para la próxima iteración
            start_date = start_date + relativedelta(months=1)
      return f'Listado de cuotas de  {  credit } creado correctamente'



#  Formula de calculo de mora es: precio  cuota * porcentaje de la mora * dias de atraso / dia del mes actual
def Calculadora_Moras(credit):

      hoy = datetime.now()
      año = hoy.year
      mes = hoy.month
      dia_mes_actual = calendar.monthrange(año, mes)[1]  # Obtenemos el número de días del mes actual
      cuotas = models.Cuotas.objects.filter(credit=credit, payment=False) # Filtra las cuotas no pagadas
      print(f'Dias del mes actual: { dia_mes_actual }- { cuotas }')
      for cuota in cuotas:
            if datetime.combine(cuota.end_date, datetime.min.time()) < datetime.now(): # Si la fecha de la cuota es menor a la fecha actual se calcula la mora
                  dias_atraso = (datetime.now() - datetime.combine(cuota.end_date, datetime.min.time())).days
                  intereses = credit.intereses / 100
                  cuota.mora = cuota.monto * intereses * dias_atraso / dia_mes_actual
                  cuota.monto_mas_mora = cuota.monto +  cuota.mora - cuota.abono  # Se suma la mora al monto de la cuota
                  cuota.save()
                  print(f'Calculo de mora de { cuota } creado correctamente')
      return f'Calculo de moras de { credit } creado correctamente'