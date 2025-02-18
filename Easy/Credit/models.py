from django.db import models
from Client.models import Client  
from .mixing import Opciones

class Credit(models.Model):
      # Cliente asociado al credito
            client = models.ForeignKey(Client, related_name='Cliente', on_delete=models.CASCADE,  verbose_name='Credito de un cliente')
      
      # Detalles del credito
            capital = models.CharField(default='', max_length=50) # Capital otorgado
            cuotas = models.IntegerField(default=4) # Cuotas
            intereses = models.IntegerField(default=15)  # Interes 
            frecuencia = models.CharField(choices=Opciones.FRECUENCIA, max_length=50) # Frecuencia de cobro

      # Fechas y modo de pagos
            start_date = models.DateField(auto_now=True) # Inicio de credito
            day_pay = models.IntegerField(default=30) #Dia de pago
            metodo = models.CharField(max_length=50, choices=Opciones.METODO) # Metodo de intereses

            def __str__(self):
                  return f'{self.client} - {self.capital} - {self.cuotas} - {self.intereses} - {self.frecuencia} - {self.metodo} - {self.start_date}'
            


class Cuotas(models.Model):
      # Credito asociado
            credit = models.ForeignKey(Credit, related_name='Cuotas', on_delete=models.CASCADE, verbose_name='Cuotas de un credito')
            
      # Detalles
            monto = models.IntegerField(default=0)
            abono = models.IntegerField(default=0)
            mora = models.IntegerField(default=0)
            
      # Fechas
            start_date = models.DateField()
            end_date = models.DateField()

      # Estado
            pagado = models.BooleanField(default=False)

            def __str__(self):
                  return f'{self.credit} - {self.monto} - {self.abono} - {self.mora} - {self.start_date} - {self.end_date} - {self.pagado}'


      



