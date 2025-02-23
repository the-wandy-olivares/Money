from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
      # Datos de la empresa
            name = models.CharField(max_length=100, default='Nombre de la empresa')
            description = models.TextField(blank=True, null=True, default='Préstamos rápidos y seguros')
            address = models.TextField(blank=True, null=True)
            phone = models.CharField(max_length=15, default='', blank=True, null=True)
            rnc = models.CharField(max_length=15, default='', blank=True, null=True)
      # Imagenes de la empresa
            logo = models.ImageField(upload_to='company/logos/', blank=True, null=True)
            img_portada = models.ImageField(upload_to='company/portada/', blank=True, null=True)
      # Redes sociales
            email = models.EmailField(blank=True, null=True)
            instagram = models.URLField(blank=True, null=True)
            facebook = models.URLField(blank=True, null=True)
      # Datos de la empresa
            date = models.DateField(auto_now=True)
            updated_at = models.DateTimeField(auto_now=True)
            is_active = models.BooleanField(default=True)
      # Interes de la empresa
            interes = models.IntegerField(blank=True, null=True)
            porcentaje_mora = models.IntegerField(blank=True, null=True)


            def __str__(self):
                  return f'{self.name} - {self.date} { "Activo" if self.is_active else "Inactivo" }'


class Configuration(models.Model):  
      # Relacion con la empresa
            company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='configuration')
      # Barra de navegacion
            navbar_dynami = models.BooleanField(default=False)
      # Tema de la aplicacion
            theme = models.CharField(max_length=10, default='light')

      # Notificaciones
            notificaciones = models.BooleanField(default=True)


      

            def __str__(self):
                  return f'{self.company.name}' 
            
# More es cargara con todos los datos del User empresa que pertence ajustes y de mas
class More(models.Model):
      # Relacion con la empresa
            company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='company')
      # Relacion con los usuario
            user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='more', null=True, blank=True)
            img = models.ImageField(upload_to='more/img/', blank=True, null=True)

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
      

