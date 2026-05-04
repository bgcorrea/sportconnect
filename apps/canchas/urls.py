from django.urls import path, include
from apps.canchas import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'canchas'

cancha_patterns = [
    path('inicio/', views.cancha_list, name='home'),
    path('<int:pk>/', views.cancha_detail, name='cancha-detail'),
    path('crear/', views.cancha_create, name='cancha-create'),
    path('<int:pk>/editar/', views.cancha_update, name='cancha-edit'),
    path('<int:pk>/eliminar/', views.cancha_delete, name='cancha-delete'),
]

urlpatterns = [
    path('', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('deportes/', views.deporte_list, name='deporte-list'),
    path('reservas/', views.reserva_list, name='reserva-list'),
    path('reservas/crear/', views.reserva_create, name='reserva-create'),
    path('canchas/', include(cancha_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
