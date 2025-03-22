from django.db import models
from django.contrib.auth.models import User
from Company.models import Company
from .mixin import CHOICES



class Client(models.Model):
      # Compañia a la que pertenece
            company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients',
                                    verbose_name='Empresa', blank=True, null=True)

      # Datos personales
            name = models.CharField(max_length=100, default='', verbose_name='Nombre', blank=True, null=True)
            last_name = models.CharField(max_length=100, default='' ,verbose_name='Apellido', blank=True, null=True)
            dni = models.CharField(max_length=15, verbose_name='DNI', null=True)
            age = models.IntegerField(choices=CHOICES.AGE, verbose_name='Edad', blank=True, null=True)
            sexo = models.CharField( choices= CHOICES.SEXO,  max_length=1, verbose_name='Sexo', blank=True, null=True)
            phone = models.CharField(max_length=20, default='', verbose_name='Teléfono', blank=True, null=True)
            email = models.EmailField(verbose_name='Correo electrónico', default='', blank=True, null=True)
            img = models.ImageField(upload_to='clients/', verbose_name='Imagen', blank=True, null=True)
      # Dirección
            municipios = models.CharField(max_length=100, default='', verbose_name='Municipios', blank=True, null=True)
            province = models.CharField( choices=CHOICES.PROVINCIAS,default='',  max_length=100, verbose_name='Estado', blank=True, null=True)

      # Datos de registro
            date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro', blank=True, null=True)
            is_active = models.BooleanField(default=True, verbose_name='Activo', blank=True, null=True)


            def __str__(self):
                    return f'{self.name} {self.last_name} - {self.dni}'
            
      



      

