from django.conf.urls import url
from apps.adopciones.views import index, SolicitudList, SolicitudCreate

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitudes/$',SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitudes/nueva$',SolicitudCreate.as_view(), name='solicitud_crear'),
]
