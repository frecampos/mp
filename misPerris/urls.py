from django.contrib import admin
from django.urls import path, include
from .views import galerias, insertar_imagen,devolver,adm_usuario,adoptar, formulario_modificar, buscar, crear_usuario, cerrar_sesion, login, filtro_tipo_boton,filtro_descripcion,filtro_tipo,detalle_mascota,index, galerias, formulario,eliminar_mascota

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galerias,name='GALE'),
    path('formulario/',formulario, name='FORMU'),
    path('eliminar_mascota/<id>/',eliminar_mascota,name='ELIM'),
    path('detalle/<id>/',detalle_mascota,name='DM'),
    path('filtro_tipo/',filtro_tipo,name='FILTROT'),
    path('filtro_desc/',filtro_descripcion,name='FILTROD'),
    path('filtro_tipo_mascota/<id>/',filtro_tipo_boton,name='FILTROTM'),
    path('login/',login,name='LOGIN'),
    path('logout/',cerrar_sesion,name='CERRAR'),
    path('crear_usuario/',crear_usuario,name='CREARU'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',formulario_modificar,name='MODI'),
    path('adoptar/<id>/',adoptar,name='ADOPTAR'),
    path('adm_usuario/',adm_usuario,name='ADMUSER'),
    path('devolver/<id>/',devolver,name='DEVOLVER'),
    path('insertar_imagen/',insertar_imagen,name='INSERTIMAGEN'),
]
