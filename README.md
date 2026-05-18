# simple-crud-django
Simple CRUD con django, utilizando vistas basadas en funciones y autentificacion 


1. Crear entorno virtual `virtualenv nombre-entorno`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Realizar migraciones `python manage.py makemigrations && python manage.py migrate`
4. Correr servidor `python manage.py runserver`

## Despliegue en producción

**URL pública:** https://web-production-1d92a.up.railway.app

**Stack:** Railway + PostgreSQL gestionada + WhiteNoise + Gunicorn

### Variables de entorno requeridas

| Variable | Descripción |
|----------|-------------|
| `SECRET_KEY` | Clave secreta de Django (generar una nueva para producción) |
| `DEBUG` | `False` en producción |
| `ALLOWED_HOSTS` | Hosts permitidos separados por coma |
| `DATABASE_URL` | URL de conexión PostgreSQL (Railway la inyecta automáticamente via reference) |

### Credenciales demo

- **Usuario:** `demo`
- **Contraseña:** `sportconnect2026`

### Proveedores soportados

El settings.py detecta el proveedor automáticamente via variables de entorno:
- **Railway:** lee `RAILWAY_PUBLIC_DOMAIN` (inyectada por Railway)
- **Render:** lee `RENDER_EXTERNAL_HOSTNAME` (inyectada por Render, alternativa documentada)
