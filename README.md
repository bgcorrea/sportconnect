# simple-crud-django
Simple CRUD con django, utilizando vistas basadas en funciones y autentificacion 


1. Crear entorno virtual `virtualenv nombre-entorno`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Realizar migraciones `python manage.py makemigrations && python manage.py migrate`
4. Correr servidor `python manage.py runserver`

## Despliegue en producción

**URL pública:** https://sportconnect.onrender.com

**Stack:** Render Web Service + PostgreSQL gestionada + WhiteNoise + Gunicorn

### Variables de entorno requeridas

| Variable | Descripción |
|----------|-------------|
| `SECRET_KEY` | Clave secreta de Django (generar una nueva para producción) |
| `DEBUG` | `False` en producción |
| `ALLOWED_HOSTS` | Hosts permitidos separados por coma |
| `DATABASE_URL` | URL de conexión PostgreSQL (la provee Render automáticamente) |

### Credenciales demo

- **Usuario:** `demo`
- **Contraseña:** `sportconnect2026`

### Nota sobre cold start

El plan gratuito de Render suspende el servicio tras 15 minutos de inactividad. El primer request tras la suspensión tarda entre 30 y 60 segundos en responder (arranque en frío). Esto es comportamiento esperado.
