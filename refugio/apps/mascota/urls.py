from django.conf.urls import url
from apps.mascota.views import MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete
urlpatterns = [

    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),


]
