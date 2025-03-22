from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
      class Meta:
            model = Client
            fields = [
                  'company', 'name', 'last_name', 'dni', 'age', 'sexo', 
                  'phone', 'email', 'municipios', 'province', 'is_active', 'img'
            ]
            widgets = {
                  'company': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar Empresa'}),
                  'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Nombre'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Apellido'}),
                  'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Cedula (obligatorio)'}),
                  'age': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Seleccionar Edad'}),
                  'sexo': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Seleccionar Género'}),
                  'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '  Teléfono personal'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' Correo '}),
                  'municipios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipio '}),
                  'province': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Seleccionar Provincia'}),
                  'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                  'img': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen '})
            }