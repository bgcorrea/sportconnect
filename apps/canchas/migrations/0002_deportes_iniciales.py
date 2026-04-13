from django.db import migrations


DEPORTES = [
    {"name": "Fútbol",       "descripcion": "Deporte de equipo con balón",          "min_jugadores": 10, "max_jugadores": 22},
    {"name": "Básquetbol",   "descripcion": "Deporte de canasta",                    "min_jugadores": 6,  "max_jugadores": 10},
    {"name": "Tenis",        "descripcion": "Deporte de raqueta individual o doble", "min_jugadores": 2,  "max_jugadores": 4},
    {"name": "Voleibol",     "descripcion": "Deporte de red por equipos",            "min_jugadores": 6,  "max_jugadores": 12},
    {"name": "Pádel",        "descripcion": "Deporte de raqueta en pareja",          "min_jugadores": 2,  "max_jugadores": 4},
    {"name": "Fútbol sala",  "descripcion": "Fútbol en cancha reducida cubierta",    "min_jugadores": 6,  "max_jugadores": 10},
]


def crear_deportes(apps, schema_editor):
    Deporte = apps.get_model("canchas", "Deporte")
    for d in DEPORTES:
        Deporte.objects.get_or_create(name=d["name"], defaults=d)


def eliminar_deportes(apps, schema_editor):
    Deporte = apps.get_model("canchas", "Deporte")
    Deporte.objects.filter(name__in=[d["name"] for d in DEPORTES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("canchas", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(crear_deportes, eliminar_deportes),
    ]
