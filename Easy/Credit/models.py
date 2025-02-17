from django.db import models
from Client.models import Client  
from .mixing import Opciones

class Credit(models.Model):
      # Cliente asociado
            client = models.ForeignKey(Client, related_name='Cliente', on_delete=models.CASCADE,
                                    verbose_name='Credito de un cliente')
      
      # Detalles
            capital = models.IntegerField(default=0)
            cuotas = models.IntegerField(default=1)
            intereses = models.IntegerField(default=15) 
            frecuecia = models.CharField(choices=Opciones.FRECUENCIA, max_length=50, default='M') 

      # Fechas
            start_date = models.DateField(auto_now=True)

      # Metodo de pago
            metodo = models.CharField(max_length=50, default='Frances', choices=Opciones.METODO)

            def __str__(self):
                  return f'{self.client} - {self.capital} - {self.cuotas} - {self.intereses} - {self.frecuecia} - {self.metodo} - {self.start_date}'
            


class Cuotas(models.Model):
      # Credito asociado
            credit = models.ForeignKey(Credit, related_name='Cuotas', on_delete=models.CASCADE,
                                    verbose_name='Cuotas de un credito')
            
      # Detalles
            monto = models.IntegerField(default=0)
            abono = models.IntegerField(default=0)
            mora = models.IntegerField(default=0)
            
      # Fechas
            start_date = models.DateField(auto_now=True)
            end_date = models.DateField(auto_now=True)

      # Estado
            pagado = models.BooleanField(default=False)

            def __str__(self):
                  return f'{self.credit} - {self.monto} - {self.abono} - {self.mora} - {self.start_date} - {self.end_date} - {self.pagado}'


      



