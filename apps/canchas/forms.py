from django import forms
from .models import Cancha, Reserva


class CanchaForm(forms.ModelForm):
    class Meta:
        model  = Cancha
        fields = ["name", "descripcion", "precio_hora", "deporte", "imagen"]


class ReservaForm(forms.ModelForm):
    class Meta:
        model  = Reserva
        fields = ["cancha", "fecha", "hora_inicio", "hora_fin"]


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
