from django import forms
from .models import Credit

class CreditForm(forms.ModelForm):
      class Meta:
            model = Credit
            fields = ['client', 'capital', 'cuotas', 'intereses', 'frecuencia', 'metodo']
            widgets = {
                    'client': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Seleccionar Cliente'}),
                    'capital': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Capital' }),
                    'cuotas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero de cuotas' }),
                    'intereses': forms.NumberInput(attrs={'class': 'form-control ' }),
                    'frecuencia': forms.Select(attrs={'class': 'form-control form-select'}),
                    'metodo': forms.Select(attrs={'class': 'form-control form-select'}),
            }