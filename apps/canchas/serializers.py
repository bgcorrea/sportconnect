from rest_framework import serializers
from .models import Deporte, Cancha


class DeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deporte
        fields = ["id", "name", "descripcion", "min_jugadores", "max_jugadores"]


class CanchaSerializer(serializers.ModelSerializer):
    deporte = DeporteSerializer(read_only=True)
    deporte_id = serializers.IntegerField(write_only=True, required=False)
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Cancha
        fields = [
            "id", "name", "descripcion", "precio_hora",
            "deporte", "deporte_id",
            "activa", "direccion", "capacidad", "imagen",
        ]

    def get_imagen(self, obj):
        if not obj.imagen:
            return None
        request = self.context.get("request")
        url = obj.imagen.url
        if request:
            return request.build_absolute_uri(url)
        return url
