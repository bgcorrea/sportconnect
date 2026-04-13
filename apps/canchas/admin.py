from django.contrib import admin
from .models import Deporte, Cancha, Reserva


@admin.register(Deporte, Cancha, Reserva)
class BaseAdminRegister(admin.ModelAdmin):
    pass
