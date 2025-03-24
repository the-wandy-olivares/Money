from django import forms
from . import models 

class Inversion(forms.ModelForm):
      class Meta:
            model = models.Inversion
            fields = [
                  'company', 'name',  'description', 'mount_inversion', 
                  'mount_retorno', 'mount_disponible', 'mount_prestado'
            ]
            widgets = {
                  'company': forms.Select(attrs={'class': 'form-control',} ),
                  'name': forms.TextInput(attrs={'class': 'form-control',} ),
                  'description': forms.Textarea(attrs={'class': 'form-control',} ),
                  'mount_inversion': forms.NumberInput(attrs={'class': 'form-control',} ),
                  'mount_retorno': forms.NumberInput(attrs={'class': 'form-control',} ),
                  'mount_disponible': forms.NumberInput(attrs={'class': 'form-control',} ),
                  'mount_prestado': forms.NumberInput(attrs={'class': 'form-control',} ),
            }     