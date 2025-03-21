from django.db import models
from django.contrib.auth.models import User
from Company.models import Company

# Caja de la compañia
class Box(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boxes', 
      null=True, blank=True)
      company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='boxes')
      # Estado de caja 
      open = models.BooleanField(default=True)
      date_opening = models.DateTimeField(auto_now_add=True)
      date_close = models.DateTimeField(null=True, blank=True)

      def __str__(self):
            return f" Caja {'abierta' if self.open else ' cerrada'} por {self.user.first_name} {self.user.last_name}"



# Movimientos 
class Movements(models.Model):
      #  Tipo de movimiento
      TYPE_CHOICE = [
            ('ingreso', 'Ingreso'), ('gasto', 'Gasto'), ('egreso', 'Egreso'), 
      ]
      # Movimientos de caja
      box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='movements', 
      null=True, blank=True)
      type = models.CharField(max_length=15, choices=TYPE_CHOICE)
      mount = models.IntegerField(default=0, blank=False, null=False)
      full_name = models.CharField(max_length=50, default='...', blank=True, null=True) 
      description = models.TextField(default='...', blank=True, null=True)
      date = models.DateTimeField(auto_now_add=True)
      # Historial de movientos
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_movements',
      null=True, blank=True)

      def __str__(self):
            return f"{self.type.capitalize()} de {'Efectuando caja' if self.mount else 'Movimiento'} el {self.date}"