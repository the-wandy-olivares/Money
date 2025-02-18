from dateutil.relativedelta import relativedelta
from calendar import monthrange
from datetime import datetime, timedelta
from . import models

class Opciones:
      FRECUENCIA = [ 
            ('mensual', 'Mensuales '), ('semanal', 'Semanales' ), ('quincenal', 'Quincenales')
      ]

      METODO = [ ('frances', 'Frances'), ( 'americano', 'Americano') ]



        
def Calculadora_Intereses( capital_, cuotas_, tasa_, credit):
      capital = int(capital_.replace(',', ''))



      cuotas = cuotas_
      tasa = int(tasa_)
      tasa = tasa / 100
      cuota = capital * tasa / (1 - (1 + tasa) ** -cuotas)
      saldo = capital
      day_pay = credit.day_pay 
      start_date = credit.start_date

      print(cuota)
      for mes in range(1, cuotas + 1):
            interes = saldo * tasa
            amortizacion_capital = cuota - interes
            saldo -= amortizacion_capital


            # Ajusta el día al valor de day_pay para start_date
            last_day_of_month = monthrange(start_date.year, start_date.month)[1]
            if day_pay > last_day_of_month:
                  start_date = start_date.replace(day=last_day_of_month)
            else:
                  start_date = start_date.replace(day=day_pay)
            
            # Ajusta el end_date al valor de day_pay más 5
            end_date = start_date + timedelta(days=5)
            if not credit.pk:
                  credit.save()
            count_cuotas = models.Cuotas(
                  credit=credit,  monto=round(cuota, 2) ,
                  start_date=start_date,   end_date=end_date,
            )
            count_cuotas.save()

      # Incrementar el mes para la próxima iteración
            start_date = start_date + relativedelta(months=1)
      return f'Listado de cuotas de  {  credit } creado correctamente'
