from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Plans(models.Model):
      name = models.CharField(max_length=50)
      price = models.IntegerField(blank=True, null=True)
      description = models.TextField(blank=True, max_length=70)

      is_active = models.BooleanField(default=True)
      date = models.DateField(auto_now_add=True)

      # Frecuencia de pagos  del plan
      FREQUENCY_PAY = [
            ('mes', 'Mensual'),
            ('trimestral', 'Trimestre'),
            ('anual', 'Anual'),
      ]
      frequency_pay = models.CharField(max_length=20, choices=FREQUENCY_PAY, default='mes')


      def __str__(self):
            return f'{self.name} - {self.price} - {self.is_active if 'Activo' else 'Desativado'}'
      

class Carateristica(models.Model):
      plan = models.ForeignKey(Plans, on_delete=models.CASCADE, blank=True,
            related_name='carateristicas')
      name = models.CharField(max_length=50)
      is_active = models.BooleanField(default=True)


      def __str__(self):
            return f'{self.plan.name} - {self.name} { self.is_active}'

class Membership(models.Model):
      # Relación con el usuario
      user = models.OneToOneField(
            User,   on_delete=models.CASCADE, 
            related_name='membership', 
            blank=True, null=True  # Permitir valores nulos si no está asociado a ningún usuario
      )
      plan = models.ForeignKey(
            Plans, on_delete=models.SET_NULL,  # Si se elimina el plan, la membresía queda con valor nulo
            related_name='memberships', 
            blank=True,  null=True
      )
      
      start_date = models.DateField(default=timezone.now)
      duration_days = models.IntegerField(default=30)  # Duración predeterminada en días
      expiration_date = models.DateField(blank=True, null=True)

      # Estado de la membresía
      is_active = models.BooleanField(default=True)

      def __str__(self):
            return f'{self.user.username if self.user else "Sin usuario"} - {self.plan.name if self.plan else "Sin plan"} - {"Activa" if self.is_active else "Inactiva"}'
      



class Payment(models.Model):
      membership = models.ForeignKey(
            Membership, on_delete=models.CASCADE,  
            related_name='membership', 
            blank=True,  null=True
      )
      name_plan = models.CharField(max_length=50)
      price_plan = models.IntegerField(default=0)
      id_plan = models.IntegerField(default=0)
      id_user = models.IntegerField(default=0)

      start_date = models.DateField(default=timezone.now)
      duration_days = models.IntegerField(default=30)  # Duración predeterminada en días
      expiration_date = models.DateField(blank=True, null=True)

      invoice = models.CharField(max_length=100, unique=True, default='')  # Agrega el campo de factura
      STATUS_CHOICES = [
                  ('pending', 'Pendiente'),
                  ('paid', 'Pagado'),
                  ('failed', 'Fallido'),
            ]
      status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

      # Estado de la membresía
      is_active = models.BooleanField(default=True)


      def __str__(self):
            return f'Plan{self.name_plan} - {self.price_plan} expira el {self.expiration_date}'