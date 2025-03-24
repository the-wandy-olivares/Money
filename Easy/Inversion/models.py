from django.db import models
from Company.models import Company


class Inversion(models.Model):
      # Company that made the inversion
      company = models.ForeignKey(Company, on_delete=models.CASCADE, 
      related_name="inversiones", blank=True, null=True)
      name = models.CharField(max_length=50, default="Nombra la inversion", blank=True, null=True)
      description = models.TextField(default="Descripcion (opcional)", blank=True)
      # Inversion inicial y retorno
      mount_inversion = models.IntegerField(default=0, blank=True, null=True)
      mount_retorno = models.IntegerField(default=0, blank=True, null=True)

      # Inversion disponible
      mount_disponible = models.IntegerField(default=0, blank=True, null=True)
      # Monto prestado
      mount_prestado = models.IntegerField(default=0, blank=True, null=True)

      date = models.DateField(auto_now_add=True)
      created = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True)

      is_active = models.BooleanField(default=True)
      
      def __str__(self):
            return f'{self.name} - {self.company.name}'