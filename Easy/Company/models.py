from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
      # Relacion con el usuario
            user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
      # Datos de la empresa
            name = models.CharField(max_length=100)
            address = models.TextField()
            phone = models.CharField(max_length=15)
            rnc = models.CharField(max_length=15)
      # Imagenes de la empresa
            logo = models.ImageField(upload_to='company/logos/')
            img_portada = models.ImageField(upload_to='company/portada/')
      # Redes sociales
            email = models.EmailField()
            instagram = models.URLField()
            facebook = models.URLField()
      # Datos de la empresa
            date = models.DateField(auto_now=True)
            updated_at = models.DateTimeField(auto_now=True)
            is_active = models.BooleanField(default=True)

            def __str__(self):
                  return f'{self.name}- {self.user.first_name} {self.user.last_name} - {self.date}'


class Configuration(models.Model):  
      # Relacion con la empresa
            company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='configuration')
      # Barra de navegacion
            navbar_dynami = models.BooleanField(default=False)
      # Tema de la aplicacion
            theme = models.CharField(max_length=10, default='light')

      # Interes de la empresa
            interes = models.IntegerField(default=0)
            porcentaje_mora = models.IntegerField(default=0)

      # Notificaciones
            notificaciones = models.BooleanField(default=True)


      

            def __str__(self):
                  return f'{self.company.name}' 
            
      
class Roles(models.Model):
      # Relacion con los usuario
            user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role_company', null=True, blank=True)

            ROLE_CHOICES = [
                  ('administrador', 'Administrador'),
                  ('gerente', 'Gerente'),
                  ('empleado', 'Empleado'),
                  ('contador', 'Contador'),
            ]
            role = models.CharField(max_length=20, choices=ROLE_CHOICES)
            description = models.TextField()
            date = models.DateField(auto_now=True)
            updated_at = models.DateTimeField(auto_now=True)
            is_active = models.BooleanField(default=True)

            def __str__(self):
                  if self.user:
                        f = f'{self.role} - {self.user} {self.user}'
                  else:
                        f = f'{self.role}'
                  return f
      

