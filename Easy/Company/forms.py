from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
      class Meta:
            model = Company
            fields = [
                  'name', 'description', 'address', 'phone', 'rnc', 
                  'logo', 'img_portada', 'email', 'instagram', 
                  'facebook', 'is_active',
                  'interes', 'porcentaje_mora'
            ]

      def __init__(self, *args, **kwargs):
            super(CompanyForm, self).__init__(*args, **kwargs)
            placeholders = {
                  'name': 'Nombre de la empresa',
                  'description': 'Descripción de la empresa',
                  'address': 'Dirección de la empresa',
                  'phone': 'Número de teléfono',
                  'rnc': 'RNC',
                  'logo': 'Suba el logo',
                  'img_portada': 'Suba la imagen de portada',
                  'email': 'correo electrónico',
                  'instagram': 'Usuario de Instagram',
                  'facebook': 'Usuario de Facebook',
                  'is_active': '¿Está activa la empresa?',
                  'interes': 'Tasa de interés',
                  'porcentaje_mora': 'Porcentaje de mora diaria' 
            }
            for field_name, field in self.fields.items():
                  field.widget.attrs.update({'class': 'form-control', 'placeholder': placeholders.get(field_name, '')})