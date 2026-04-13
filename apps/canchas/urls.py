from django.conf.urls import url, include
from apps.canchas import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'canchas'

cancha_patterns = [
    url(r'^inicio/$', views.cancha_list, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.cancha_detail, name='cancha-detail'),
    url(r'^crear/$', views.cancha_create, name='cancha-create'),
    url(r'^(?P<pk>[0-9]+)/editar/$', views.cancha_update, name='cancha-edit'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.cancha_delete, name='cancha-delete'),
]

urlpatterns = [
    url(r'^$', views.log_in, name='log-in'),
    url(r'^log-out/$', views.log_out, name='log-out'),
    url(r'^deportes/$', views.deporte_list, name='deporte-list'),
    url(r'^reservas/$', views.reserva_list, name='reserva-list'),
    url(r'^reservas/crear/$', views.reserva_create, name='reserva-create'),
    url(r'^canchas/', include(cancha_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
