from django.db import models
from Client.models import Client  
from Company.models import Company
from .mixing import Opciones

class Credit(models.Model):
      # Compañia asociada al credito
            company = models.ForeignKey(Company, related_name='Compañia', on_delete=models.CASCADE, verbose_name='Compañia asociada al credito', blank=True, null=True, default=None)
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

      # Estado
            payment = models.BooleanField(default=False) # Estado de pago
            last_pay = models.DateField(auto_now=True) # Ultimo pago
            is_active = models.BooleanField(default=True) # Estado del credito

            def __str__(self):
                  return f'{self.client} - {self.capital} - {self.cuotas} - {self.intereses} - {self.frecuencia} - {self.metodo} - {self.start_date}'
            


class Cuotas(models.Model):
      # Credito asociado
            credit = models.ForeignKey(Credit, related_name='Cuotas', on_delete=models.CASCADE, verbose_name='Cuotas de un credito')
            
      # Detalles
            monto = models.IntegerField(default=0)  # Valores fijos
            abono = models.IntegerField(default=0) # Valores fijos
            mora = models.IntegerField(default=0) # Valores fijos
            monto_mas_mora = models.IntegerField(default=0) # Valores variables se le suma la mora al monto de la cuota
            
      # Fechas
            start_date = models.DateField()
            end_date = models.DateField()

      # Estado
            payment = models.BooleanField(default=False)

            def __str__(self):
                  return f'{self.credit} - {self.monto} - {self.abono} - {self.mora} - {self.start_date} - {self.end_date} - {self.payment}'


      



