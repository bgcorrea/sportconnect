from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class BaseName(models.Model):
    name    = models.CharField(max_length=150, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Deporte(BaseName):
    descripcion   = models.TextField(blank=True, verbose_name="Descripción")
    min_jugadores = models.IntegerField(default=2, verbose_name="Mínimo jugadores")
    max_jugadores = models.IntegerField(default=22, verbose_name="Máximo jugadores")

    class Meta:
        verbose_name = "Deporte"
        verbose_name_plural = "Deportes"


class Cancha(BaseName):
    descripcion  = models.TextField(blank=True, verbose_name="Descripción")
    precio_hora  = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio por hora")
    deporte      = models.ForeignKey(Deporte, on_delete=models.CASCADE, verbose_name="Deporte")
    imagen       = models.ImageField(upload_to="canchas/", blank=True, verbose_name="Imagen")
    activa       = models.BooleanField(default=True, verbose_name="Activa")

    class Meta:
        verbose_name = "Cancha"
        verbose_name_plural = "Canchas"

    def get_edit_url(self):
        return reverse_lazy("canchas:cancha-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("canchas:cancha-delete", kwargs={"pk": self.pk})

    def get_detail_url(self):
        return reverse_lazy("canchas:cancha-detail", kwargs={"pk": self.pk})


class Reserva(models.Model):
    cancha      = models.ForeignKey(Cancha, on_delete=models.CASCADE, verbose_name="Cancha")
    usuario     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha       = models.DateField(verbose_name="Fecha")
    hora_inicio = models.TimeField(verbose_name="Hora inicio")
    hora_fin    = models.TimeField(verbose_name="Hora fin")
    estado      = models.CharField(max_length=20, default="pendiente", verbose_name="Estado")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"{self.cancha} - {self.fecha} {self.hora_inicio}"
