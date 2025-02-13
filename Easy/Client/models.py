from django.db import models
from django.contrib.auth.models import User
from Company.models import Company
from .mixin import CHOICES



class Client(models.Model, CHOICES):
      # Compañia a la que pertenece
            company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients',
                                    verbose_name='Empresa', blank=True, null=True)

      # Datos personales
            name = models.CharField(max_length=100, verbose_name='Nombre', blank=True, null=True)
            last_name = models.CharField(max_length=100, verbose_name='Apellido', blank=True, null=True)
            dni = models.CharField(max_length=10, verbose_name='DNI', blank=True, null=True)
            age = models.IntegerField(choices=CHOICES.AGE_CHOICES, verbose_name='Edad', blank=True, null=True)
            sexo = models.CharField( choices= CHOICES.SEXO_CHOICES, max_length=1, verbose_name='Sexo', blank=True, null=True)
            phone = models.CharField(max_length=20, verbose_name='Teléfono', blank=True, null=True)
            email = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)

      # Dirección
            address = models.TextField(verbose_name='Dirección', blank=True, null=True)
            city = models.CharField(max_length=100, verbose_name='Ciudad', blank=True, null=True)
            province = models.CharField( choices=CHOICES.PROVINCIAS, max_length=100, verbose_name='Estado', blank=True, null=True)

      # Datos de registro
            date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro', blank=True, null=True)
            is_active = models.BooleanField(default=True, verbose_name='Activo', blank=True, null=True)

      

