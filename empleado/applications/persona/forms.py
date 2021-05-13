from django import forms
from .models import Persona

class EmpleadoForm(forms.ModelForm):
    """Formulario definicion para  Persona."""

    class Meta:
        """Meta definition for EmpleadoForm."""
        model = Persona
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',

            )
        widgets={
            'habilidades':forms.CheckboxSelectMultiple()
        }
