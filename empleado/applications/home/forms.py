from django import forms
from .models import Prueba
class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
            )
        widgets={
            'titulo':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese titulo'
                }
            )
        }
    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad']
        if cantidad<10:
            raise forms.ValidationError('Ingrese una cantidad mayor a 10')
        return cantidad