from django.db import models
from Company.models import Company


class Inversion(models.Model):
      # Company that made the inversion
      company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="inversiones")
      name = models.CharField(max_length=50, default="Inversion incial", blank=True, null=True)
      description = models.TextField(default="", blank=True)
      # Inversion inicial y retorno
      mount_inversion = models.IntegerField(default=0, blank=True, null=True)
      mount_retorno = models.IntegerField(default=0, blank=True, null=True)

      date = models.DateField(auto_now_add=True)
      created = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True)
      
      def __str__(self):
            return f'{self.name} - {self.company.name}'