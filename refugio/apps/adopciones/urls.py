from django.conf.urls import url
from apps.adopciones.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitudes/$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitudes/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitudes/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitudes/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]
