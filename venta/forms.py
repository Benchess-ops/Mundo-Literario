from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nombre_completo', 'telefono', 'direccion']
        widgets = {
            'password': forms.PasswordInput(),
        }
